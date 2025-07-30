from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
    # # MySQL Database settings
    # MYSQL_HOST: str = os.getenv("MYSQL_HOST")
    # MYSQL_PORT: int = os.getenv("MYSQL_PORT")
    # MYSQL_USER: str = os.getenv("MYSQL_USER")
    # MYSQL_PASSWORD: str = os.getenv("MYSQL_PASSWORD")
    # MYSQL_DATABASE: str = os.getenv("MYSQL_DATABASE")
    
    HOSTED_MYSQL_URL: str = os.getenv("HOSTED_MYSQL_URL")
    # Construct MySQL URL
    # @property
    # def MYSQL_DATABASE_URL(self) -> str:
    #     return f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_HOST}:{self.MYSQL_PORT}/{self.MYSQL_DATABASE}"
    
    # # ClickHouse Database settings
    # CLICKHOUSE_HOST: str = os.getenv("CLICKHOUSE_HOST")
    # CLICKHOUSE_PORT: int = os.getenv("CLICKHOUSE_PORT")
    # CLICKHOUSE_HTTP_PORT: int = os.getenv("CLICKHOUSE_HTTP_PORT")
    # CLICKHOUSE_USER: str = os.getenv("CLICKHOUSE_USER")
    # CLICKHOUSE_PASSWORD: str = os.getenv("CLICKHOUSE_PASSWORD")
    # CLICKHOUSE_DATABASE: str = os.getenv("CLICKHOUSE_DATABASE")
    
    HOSTED_CLICKHOUSE_URL: str = os.getenv("HOSTED_CLICKHOUSE_URL")
    # Construct ClickHouse URL
    # @property
    # def CLICKHOUSE_DATABASE_URL(self) -> str:
    #     if self.CLICKHOUSE_PASSWORD:
    #         return f"clickhouse://{self.CLICKHOUSE_USER}:{self.CLICKHOUSE_PASSWORD}@{self.CLICKHOUSE_HOST}:{self.CLICKHOUSE_PORT}/{self.CLICKHOUSE_DATABASE}"
    #     else:
    #         return f"clickhouse://{self.CLICKHOUSE_USER}@{self.CLICKHOUSE_HOST}:{self.CLICKHOUSE_PORT}/{self.CLICKHOUSE_DATABASE}"
    
    # Other settings
    PORT: int = 8000
    SENTRY_DSN: str = os.getenv("SENTRY_DSN")
    
    class Config:
        env_file = ".env"

settings = Settings() 