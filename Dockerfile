FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    && apt-get clean

RUN curl -sSL https://install.python-poetry.org | python3 -

ENV PATH="/root/.local/bin:$PATH"

COPY ./poetry/pyproject.toml ./poetry/poetry.lock ./

RUN pip install --upgrade pip

RUN pip install poetry && poetry install --no-root
RUN poetry update

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

