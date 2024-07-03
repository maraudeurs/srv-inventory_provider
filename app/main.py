from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import json

from utils.config import settings
from utils.logger_config import setup_logging
import logging

from providers.scw_provider import scaleway_api_init, get_scw_zones, get_scw_instances

## Manage logging
setup_logging()
logger = logging.getLogger(__name__)

## Manage scheduler
# scheduler = BackgroundScheduler()
# scheduler.add_job(get_provider_inventory, 'interval', days=1)
# scheduler.start()

# def get_provider_inventory():

# zones = get_scw_zones()
# print(zones)

client = scaleway_api_init()
zone_list = get_scw_zones(client)
instances = get_scw_instances(client, zone_list)
print(json.dumps(instances.content, indent=4))