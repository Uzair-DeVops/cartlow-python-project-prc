from contextlib import asynccontextmanager
from fastapi import FastAPI
from .config.database import initialize_mysql_engine, initialize_clickhouse_client
from .utils.my_logger import get_logger
from .routes.migration_routes import router as migration_routes
from .config.my_settings import settings
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware


# SENTRY INITIALIZATION
# sentry_sdk.init(
#     dsn=settings.SENTRY_DSN,
#     # Add data like request headers and IP for users,
#     # see https://docs.sentry.io/platforms/python/data-mana gement/data-collected/ for more info
#     send_default_pii=True,
#     # Set traces_sample_rate to 1.0 to capture 100% of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     # https://docs.sentry.io/platforms/python/guides/fastapi/performance/
#     traces_sample_rate=1.0,
# )


# testing sentry








# Startup event
async def startup_event():
    get_logger(name="UZAIR").info("🚀 Starting up Data Migration Project...")
    
    # Initialize and store in app.state
    app.state.mysql_engine = initialize_mysql_engine()
    app.state.clickhouse_client = initialize_clickhouse_client()
    



# Shutdown event
async def shutdown_event():
    get_logger(name="UZAIR").info("🛑 Shutting down Data Migration Project...")
    
    # Cleanup - ClickHouse client doesn't need explicit closing
    # The client will be garbage collected automatically
    if hasattr(app.state, 'clickhouse_client'):
        get_logger(name="UZAIR").info("✅ ClickHouse client cleanup completed")
    if hasattr(app.state, 'mysql_engine'):
        get_logger(name="UZAIR").info("✅ MySQL engine cleanup completed")

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    await startup_event()

    # This is where the app runs (yield)
    yield 

    # Shutdown event
    await shutdown_event()

app = FastAPI(
    version="0.1.0",
    lifespan=lifespan  
)

# Include routers
app.include_router(migration_routes, prefix="/api/v1")

#MIDDLEWARES
# app.add_middleware(SentryAsgiMiddleware)


@app.get("/health")
async def health_check():
    return {"status": "The server is running successfully"}

@app.get("/sentry-debug")
async def trigger_error():
    raise Exception("This is a test exception")