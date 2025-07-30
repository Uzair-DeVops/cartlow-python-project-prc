"""
Database dependency injection utilities
"""

from typing import Generator
from fastapi import Request, Depends
from sqlmodel import Session
from clickhouse_driver import Client
from .my_logger import get_logger

def get_mysql_session(request: Request) -> Generator[Session, None, None]:
    """Get MySQL session with automatic cleanup"""
    engine = request.app.state.mysql_engine
    with Session(engine) as session:
        try:
            yield session
        except Exception as e:
            get_logger(name="UZAIR").error(f"❌ MySQL session error: {e}")
            session.rollback()
            raise
        finally:
            session.close()

def get_clickhouse_client(request: Request) -> Client:
    """Get ClickHouse client from app state"""
    return request.app.state.clickhouse_client

# Keep engine function for special cases if needed
def get_mysql_engine(request: Request):
    """Get MySQL engine from app state (for special cases)"""
    return request.app.state.mysql_engine 