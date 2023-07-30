import yaml
import logging
import subprocess

fakker_config = {}

def init_logger():
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s] - %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    logging.info("Initializing zookeeper and kafka")

def init_configs():
    with open ("config.yml", "r") as config_file:
         fakker_config = yaml.safe_load(config_file)


if (__name__ == "__main__"):
    init_logger()
    init_configs()
    logging.info(fakker_config)




