from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    db_host: str = 'localhost'
    db_user: str = 'postgres'
    db_password: str = 'root'
    db_name: str = 'item_db'
    test_db_name: str = 'testdb'
    redis_host: str = os.getenv('DOCKER_REDIS_HOST', 'localhost')
    redis_port: str = '6379'
    redis_db: str = '0'


settings = Settings()
