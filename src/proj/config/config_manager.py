
from proj.entity.entity_config import DataIngestionConfig
from proj.constants import *



class ConfigurationManager:

    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            params_filepath = CONFIG_PARAMS_PATH,
            schema_filepath = CONFIG_SCHEMA_PATH
    ):
        print(config_filepath)
        print(params_filepath)
        print(schema_filepath)

# print(CONFIG_FILE_PATH)
ConfigurationManager()