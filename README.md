# Data Migration Project


## Prerequisites

- Python 3.11 or higher
- MySQL database server
- ClickHouse database server
- `uv` package manager

## Installation

1. **Clone the repository:**

   ```bash
   git clone <your-repository-url>
   cd data_migration_project
   ```

2. **Create and activate virtual environment:**

   ```bash
   uv venv
   source .venv/bin/activate  # On Linux/macOS
   # or
   .venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies:**

   ```bash
   uv sync
   ```

## Environment Configuration

1. **Create a `.env` file in the project root:**

   ```bash
   cp .env.example .env
   ```

2. **Configure your database settings in `.env`:**

   ```env
   # MySQL Configuration
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   MYSQL_USER=your_mysql_user
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_DATABASE=your_mysql_database

   # ClickHouse Configuration
   CLICKHOUSE_HOST=localhost
   CLICKHOUSE_PORT=9000
   CLICKHOUSE_HTTP_PORT=8123
   CLICKHOUSE_USER=default
   CLICKHOUSE_PASSWORD=your_clickhouse_password
   CLICKHOUSE_DATABASE=default


   ```

## Running the Project

### Method : Using the run.py script 

```bash
uv run run.py
```



## Accessing the Application


- **Health Check:** http://localhost:8000/health

## API Endpoints

The application provides migration endpoints under `/api/v1/`:

- `POST /api/v1/migrate` - Start a data migration
- `GET /api/v1/status` - Check migration status
- `GET /api/v1/logs` - View migration logs

## Development

### Project Structure

```
data_migration_project/
├── app/
│   ├── config/          # Configuration files
│   ├── controllers/     # Business logic
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   ├── utils/           # Utility functions
│   └── views/           # View components
├── logs/                # Application logs
├── run.py              # Application entry point
└── pyproject.toml      # Project configuration
```

### Running in Development Mode

The application runs with auto-reload by default, so any changes to the code will automatically restart the server.

### Logging

Logs are written to `logs/data_migration.log` and also displayed in the console.

## Troubleshooting

1. **Database Connection Issues:**

   - Verify your database servers are running
   - Check your `.env` configuration
   - Ensure network connectivity to database hosts

2. **Port Already in Use:**

   - Change the port in `run.py` or use a different port with uvicorn
   - Kill any existing processes using port 8000

3. **Permission Issues:**
   - Ensure you have write permissions for the `logs/` directory
   - Check file permissions on your `.env` file

## Production Deployment

For production deployment:

1. Set `DEBUG=false` in your environment
2. Use a production WSGI server like Gunicorn
3. Configure proper logging
4. Set up reverse proxy (nginx/Apache)
5. Use environment variables for sensitive configuration

Example production command:

```bash
gunicorn app.app:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

## License

[Add your license information here]
