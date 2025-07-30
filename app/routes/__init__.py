"""
Routes package
Contains all API route definitions
"""

from .migration_routes import router as migration_router

__all__ = [
    "migration_router"
]