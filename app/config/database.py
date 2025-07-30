import sys
import os
from pathlib import Path
from urllib.parse import urlparse, unquote
from sqlmodel import SQLModel, create_engine, Session, text
from clickhouse_driver import Client
from .my_settings import settings
from ..utils.my_logger import get_logger


def initialize_mysql_engine():
    """
    Initialize MySQL SQLModel engine
    """
    try:
        get_logger(name="UZAIR").info("🔧 Initializing MySQL engine...")
        # Create SQLModel engine for MySQL ORM operations only
        mysql_engine = create_engine(
            settings.HOSTED_MYSQL_URL,
            echo=True,  # Set to False in production
            pool_pre_ping=True,
            pool_recycle=300,
            pool_size=10,
            max_overflow=20
        )
        # test connection by executing a simple query
        with mysql_engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        get_logger(name="UZAIR").info("✅ MySQL engine initialized successfully")
        return mysql_engine
    except Exception as e:
        get_logger(name="UZAIR").error(f"❌ Could not initialize MySQL engine: {e}")
        return None



def initialize_clickhouse_client():
    """
    Initialize ClickHouse client connection
    """
    try:
        clickhouse_url = urlparse(settings.HOSTED_CLICKHOUSE_URL)
        get_logger(name="UZAIR").info("🗄️ Initializing ClickHouse client...")
        password = unquote(clickhouse_url.password) if clickhouse_url.password else ""
        
        clickhouse_client = Client(
            host=clickhouse_url.hostname,
            port=clickhouse_url.port or 9000,
            user=clickhouse_url.username,
            password=password,
            database=clickhouse_url.path[1:] if clickhouse_url.path else 'default'
        )

        # test connection by executing a simple query
        clickhouse_client.execute('SELECT 1')
        get_logger(name="UZAIR").info("✅ ClickHouse client initialized successfully")

        
        return clickhouse_client
    except Exception as e:
        get_logger(name="UZAIR").warning(f"⚠️ Could not initialize ClickHouse client: {e}")
        return None