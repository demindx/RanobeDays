FROM python:latest

ENV PYTHONUNBUFFERED=1 \
POETRY_HOME="/opt/poetry" \
POETRY_VIRTUALENVS_CREATE=fasle

WORKDIR /code

RUN curl -sSL https://install.python-poetry.org | python
ENV PATH="$POETRY_HOME/bin:$PATH"

COPY . /code/

RUN apt-get update && apt-get install pandoc texlive-full -y

RUN poetry config virtualenvs.create false && poetry install --no-root
