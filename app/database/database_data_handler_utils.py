import datetime
from sqlalchemy.orm import Session
from database.instance_model import Instance

def manage_instance_creation_date(db: Session, instance_id) -> str:
    """
    Manage instance creation date (set creation_date if newly registered instance)

    Args:
        db : database session
        instance_id : provider instance_id

    Returns:
        str: instance creation date
    """

    ## search if instance already exist in database
    db.query(Instance).filter(Instance.provider_uuid == instance_id).first()
    # provider_uuid_query = Instance.select().where(Instance.columns.provider_uuid == instance_id)
    # provider_uuid_result = cp

    ## if exist, then get existing creation_date and leave unchanged

    ## else (not exist) then init creation_date to now
    now = datetime.datetime.now()

def manage_instance_tag(db, instance_id) -> str:
    """
    Manage instance tag (if fisrt add, set tag to null, else keep existing tag)

    Args:
        db : database session
        instance_id : provider instance_id

    Returns:
        str: instance_tag
    """

    ## search instance
    # db.query(Instance).filter(Instance.provider_uuid == instance_id).first()