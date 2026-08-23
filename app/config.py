import os

class MissingEnvironmentVariableException(Exception):
    pass

try:
    DATABASE_URL=os.environ["DATABASE_URL"]
except KeyError:

    raise MissingEnvironmentVariableException("Database URL Not found in the environment")

