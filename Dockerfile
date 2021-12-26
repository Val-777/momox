FROM python:3.9.9-slim

ENV POETRY_VERSION=1.1.4 \
    POETRY_VIRTUALENVS_CREATE=false

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /code
COPY poetry.lock pyproject.toml /code/

RUN poetry install --no-interaction --no-ansi

COPY . /code

CMD [ "poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5000" ]