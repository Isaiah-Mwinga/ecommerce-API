FROM python:3.10

# Install poetry
RUN pip install "poetry==1.1.13" && poetry config virtualenvs.create false

# Copy poetry.lock* in case it doesn't exist in the repo
COPY pyproject.toml poetry.lock* /app/

ENV PYTHONPATH=/app

WORKDIR /app/

RUN poetry install --no-root --no-dev

COPY ./docker/start.sh start.sh
RUN chmod +x start.sh

COPY . /app
EXPOSE 80

CMD ["./start.sh"]
