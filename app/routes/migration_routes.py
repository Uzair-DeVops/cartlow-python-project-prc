from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from clickhouse_connect.driver import Client
from ..utils.my_logger import get_logger
from ..controllers.migrations_controllers import orders_migration
from ..utils.database_dependency import get_mysql_session, get_clickhouse_client

router = APIRouter()


@router.get("/orders-migration")
async def orders_migration_route(
    mysql_session: Session = Depends(get_mysql_session), 
    clickhouse_client: Client = Depends(get_clickhouse_client)
):
    try:
        data = orders_migration(mysql_session, clickhouse_client)
        return {
            "message": "Orders migration completed",
            "status": "success",
            "data": data
        }
    except Exception as e:
        get_logger(name="UZAIR").error(f"Error in orders migration: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

