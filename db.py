from orator import DatabaseManager, Schema, Model

# Default settings, as per Postgres.app:
# https://postgresapp.com/
#
my_database = "mike"
my_user = "mike"
my_password = ""

DATABASES = {
    "postgres": {
        "driver": "postgres",
        "host": "localhost",
        "database": my_database,
        "user": my_user,
        "password": my_password,
        "prefix": "",
        "port": 5432
    }
}

db = DatabaseManager(DATABASES)
schema = Schema(db)
Model.set_connection_resolver(db)
