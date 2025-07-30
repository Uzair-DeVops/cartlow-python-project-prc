from sqlmodel import Session, select, text
from clickhouse_connect.driver import Client
from ..utils.my_logger import get_logger
from ..models.mysql_models import Orders

def orders_migration(mysql_session: Session, clickhouse_client: Client):
    """
    Migrate orders data from MySQL to ClickHouse
    """
    try:
        # Direct execution since session is managed by dependency
        result = mysql_session.exec(text("SELECT * FROM orders"))
        orders = [dict(row._mapping) for row in result]
        
        get_logger(name="UZAIR").info(f"Retrieved {len(orders)} orders from MySQL")
        return orders
        
        # Alternative ORM-based approach (uncomment if preferred):
        # orders = mysql_session.exec(select(Orders)).all()
        # orders_data = [order.dict() for order in orders]
        # get_logger(name="UZAIR").info(f"Retrieved {len(orders_data)} orders from MySQL")
        # return orders_data
        
    except Exception as e:
        get_logger(name="UZAIR").error(f"Error reading orders from MySQL: {str(e)}")
        raise