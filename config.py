import os

PG_HOST = os.environ.get("PG_HOST", "localhost")
REDIS_HOST = os.environ.get("REDIS_HOST", "redis")


class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://user:password@{PG_HOST}:5432/ticket_db"

    CACHE_TYPE = 'RedisCache'
    CACHE_REDIS_URL = f'redis://{REDIS_HOST}:6379/1'
