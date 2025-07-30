FROM python:3.11

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install uv && uv sync

COPY . .

RUN python -m compileall .


CMD ["uv", "run", "run.py"]