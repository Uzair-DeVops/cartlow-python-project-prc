from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseSettings):
   
    HOSTED_MYSQL_URL: str = os.getenv("HOSTED_MYSQL_URL")
   
    HOSTED_CLICKHOUSE_URL: str = os.getenv("HOSTED_CLICKHOUSE_URL")
    
    # Other settings
    PORT: int = 8000
    SENTRY_DSN: str = os.getenv("SENTRY_DSN")
    
    class Config:
        env_file = ".env"

settings = Settings() 