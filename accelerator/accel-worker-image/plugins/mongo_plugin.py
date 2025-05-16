from airflow.plugins_manager import AirflowPlugin
from airflow.models.connection import Connection
from airflow.hooks.base import BaseHook

class MongoHook(BaseHook):
    conn_name_attr = 'mongo_conn_id'
    default_conn_name = 'mongo_default'
    conn_type = 'mongodb'
    hook_name = 'MongoDB'

    def __init__(self, mongo_conn_id='mongo_default'):
        self.conn_id = mongo_conn_id
        self.connection = self.get_connection(mongo_conn_id)

    def get_uri(self):
        return f"mongodb://{self.connection.login}:{self.connection.password}@{self.connection.host}:{self.connection.port}/{self.connection.schema}"

class MongoPlugin(AirflowPlugin):
    name = "mongo_plugin"
    hooks = [MongoHook]
    connection_types = [
        {
            "conn_type": "mongodb",
            "hook_class_name": "mongo_plugin.MongoHook",
        }
    ]
