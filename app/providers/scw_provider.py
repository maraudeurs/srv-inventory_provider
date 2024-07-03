import requests
import json
from utils.config import settings
import logging

# from scaleway.apis import ComputeAPI
from scaleway import Client
from scaleway_core.bridge import ALL_ZONES
from scaleway.instance.v1.api import InstanceV1API

logger = logging.getLogger()

def scaleway_api_init():
    """init scw client based on api credentials"""
    client = Client(
        access_key=settings.scw_access_key_id,
        secret_key=settings.scw_secret_key,
        default_project_id=settings.scw_project_id,
        default_region="fr-par",
        default_zone="fr-par-1",
    )
    return client

def get_scw_zones(client: Client)-> list :
    """
    Get scw zones list

    Args:
        client : scw client

    Returns:
        list: list of scw zones
    """
    return ALL_ZONES

def get_scw_instances(client: Client, zone_list: list) -> list:
    """
    Get all scw instances

    Args:
        client : scw client

    Returns:
        list: list of scw instances
    """
    instance_api = InstanceV1API(client)
    all_zone_instance_list = []
    for zone in zone_list:
        instance_list = instance_api.list_servers_all(zone=zone).servers
        all_zone_instance_list.extend(instance_list)

    return all_zone_instance_list
