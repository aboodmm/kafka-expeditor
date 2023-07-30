import yaml
import logging
import os
import sys

fakker_config = {}

def init_logger():
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s] - %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
    logging.info("Initializing zookeeper and kafka")

def init_configs():
    with open ("./config.yml", "r") as config_file:
        global fakker_config
        fakker_config = yaml.safe_load(config_file)

def validate_configs():
    root_obj = fakker_config.get("fakker")
    broker_str = root_obj.get("broker")
    dir_str = root_obj.get("kafkadir")
    if (root_obj is None):
        sys.exit("validate_configs(): Improper config")
    if (broker_str is None or len(broker_str.strip()) < 1):
        sys.exit("validate_configs(): Improper config")
    if (dir_str is None or len(dir_str.strip()) < 1):
        sys.exit("validate_configs(): Improper config")
    return 

def get_kafka_dir():
    return fakker_config.get("fakker").get("kafkadir")

def start_zookeeper():
    kafka_dir = get_kafka_dir()
    bin_dir = kafka_dir + "/bin/"
    config_dir = kafka_dir + "/config/"
    os.popen(bin_dir + "zookeeper-server-start.sh", config_dir + "zookeeper.properties")


if (__name__ == "__main__"):
    init_logger()
    init_configs()
    validate_configs()
    start_zookeeper()




