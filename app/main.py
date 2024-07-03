from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import json

from utils.config import settings
from utils.logger_config import setup_logging
import logging

from database.dependencies import get_db
from database.database import engine, init_db
from providers.scw_provider import scaleway_api_init, get_scw_zones, get_scw_instances
from providers.ovh_provider import ovh_api_init, get_ovh_projects, get_ovh_instances, get_ovh_prices


# def cloud_inventory_job():
    ## get cloud inventory for scw provider
    # @TODO

    ## get cloud inventory for ovh provider
    # @TODO

    ## status_update
    # @TODO
    ### if instance update_date > 1 week then update status to UNREGISTERED
    ### if instance update_date > 2 week then update status to DELETED

if __name__ == "__main__":

    ## Manage logging
    setup_logging()
    logger = logging.getLogger(__name__)

    ## Manage Database
    init_db(engine)

    ## Manage scheduler
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(cloud_inventory_job, 'interval', days=1)
    # scheduler.start()

    ## testing below scw provider
    # scw_client = scaleway_api_init()
    # scw_zone_list = get_scw_zones(scw_client)
    # instances = get_scw_instances(scw_client, scw_zone_list)

    ## testing below ovh provider
    # ovh_client = ovh_api_init()
    # ovh_project_list = get_ovh_projects(ovh_client)
    # ovh_instance_list=get_ovh_instances(ovh_client, next(get_db()), ovh_project_list)