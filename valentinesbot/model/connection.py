from peewee import PostgresqlDatabase

from utils import EnvironmentVariables


env = EnvironmentVariables(
    'PG_URL',
)


connection = PostgresqlDatabase(
    database=env.PG_URL,
)

connection.connect()
