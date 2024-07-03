from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Instance(Base):
    __tablename__ = 'instances'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, index=True)
    description = Column(String)
    ip_v4 = Column(String)
    ip_v6 = Column(String)
    status = Column(String)
    main_usage = Column(String)
    location = Column(String)
    tag = Column(String)
    cloud_model = Column(String)
    cloud_provider = Column(String)
    provider_uuid = Column(String)
    instance_memory = Column(String)
    instance_cpu = Column(String)
    in_bandwidth = Column(String)
    out_bandwidth = Column(String)
    os = Column(String)
    cloud_service_type = Column(String) ## public_cloud, private_cloud, baremetal
    inventory_source_method = Column(String) ## inventory_agent, cloud_api, ... other ?
    update_date = Column(String)
    creation_date = Column(String)