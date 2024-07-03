import json
from ovh import Client, exceptions
import os
import logging
import datetime

from sqlalchemy.orm import Session

from database.instance_model import Instance
from database.database_data_handler_utils import manage_instance_creation_date
from utils.config import settings

logger = logging.getLogger()

def ovh_api_init():
    """init ovh client based on api credentials"""

    client = Client(
        endpoint = settings.ovh_endpoint,
        application_key = settings.ovh_application_key,
        application_secret = settings.ovh_application_secret,
        consumer_key = settings.ovh_consumer_key,
    )
    return client

def get_ovh_projects(client: Client)-> list :
    """
    Get ovh project list

    Args:
        client : ovh client

    Returns:
        list: list of ovh project
    """
    try:
        project_list = client.get('/cloud/project')
        return project_list
    except exceptions.APIError as e:
        print(f"Error fetching projects: {e}")
        return []

def get_ovh_instances(client: Client, db: Session, project_list: list) -> list:
    """
    Get ovh instance list

    Args:
        client : ovh client

    Returns:
        list: list of ovh instance
    """
    instancesList = []
    project_list = get_ovh_projects(client)
    for project_id in project_list:
        project = client.get(f'/cloud/project/{project_id}/')
        project_instances = client.get(f'/cloud/project/{project_id}/instance/')
        for instance in project_instances:
            instance_id = instance['id']
            instance_details = client.get(f'/cloud/project/{project_id}/instance/{instance_id}/')
            ovh_instance = Instance(
                name = instance_details.get('name'),
                description = instance_details.get('description', f'ovh server from project {project_id} '),
                ip_v4 = instance_details['ipAddresses'][0]['ip'],
                ip_v6 = instance_details['ipAddresses'][1]['ip'],
                status = instance_details['status'],
                main_usage = "" ,
                location = instance_details['region'] ,
                tag = manage_instance_tag(db, instance_id) ,
                cloud_model = instance_details['flavor']['name'] ,
                cloud_provider = "OVH" ,
                provider_uuid = instance_details['id'] ,
                instance_memory = instance_details['flavor']['ram'] ,
                instance_cpu = instance_details['flavor']['vcpus'] ,
                update_date = datetime.datetime.now() ,
                creation_date = manage_instance_creation_date(db, instance_id) ,
            )
            db.add(ovh_instance)
            db.commit()
            db.refresh(ovh_instance)
            instancesList.append(ovh_instance)

    return instancesList


		# glpi_instance = GlpiInstance(
		# 	provider = "OVH",
		# 	project = project['description'],
		# 	id = details['id'],
		# 	name = details['name'],
		# 	ipv4 = details['ipAddresses'][0]['ip'],
		# 	region = details['region'],
		# 	status = details['status'],
		# 	model = details['flavor']['name'],
		# 	vcpus = details['flavor']['vcpus'],
		# 	ram = details['flavor']['ram'],
		# 	disk = details['flavor']['disk'],
		# 	os = details['flavor']['osType'],
		# 	in_bandwidth = details['flavor']['inboundBandwidth'],
		# 	out_bandwidth = details['flavor']['outboundBandwidth'],
		# )
		# instancesList.append(glpi_instance)


