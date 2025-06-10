FROM python:3.13-alpine

RUN pip install uv

RUN uv --version

WORKDIR /app

COPY pyproject.toml uv.lock* ./

RUN uv sync --no-dev

COPY . .

CMD ["uv", "run", "main.py"]
