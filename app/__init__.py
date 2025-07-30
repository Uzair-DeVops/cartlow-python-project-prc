"""
Main application package
Contains the FastAPI app and core functionality
"""

# Core application
from .app import app

# Configuration

from .config import (
     database,
     my_settings,
     
)

# Controllers
from .controllers import (
    migrations_controllers
)

# Models
from .models import (
    mysql_models
)

# Routes
from .routes import (
    migration_routes
)


# Utilities
from .utils import (
    database_dependency,
    my_logger,

)




    

__all__ = [
    # Core application
    "app",
    # Configuration
    "database",
    "my_settings",
    # Models
    "mysql_models",
    
    # Utilities
    "database_dependency",
    "my_logger",
    
    # Controllers
    "migrations_controllers",
    
    # Routes
    "migration_routes",
] 