import yaml
import logging
import sys
from kafka import KafkaProducer
import uuid
import glob

fakker_config = {}

def init_logger():
    logging.basicConfig(format='[%(asctime)s] [%(levelname)s] - %(message)s',
                         datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)

def init_configs():
    with open ("./config.yml", "r") as config_file:
        global fakker_config
        fakker_config = yaml.safe_load(config_file)

def retrieve_conf(key):
    root_obj = fakker_config.get("fakker")
    target_obj = root_obj.get(key)
    return target_obj

def validate_configs():
    if (fakker_config is None):
        sys.exit("validate_configs(): Improper config")
    broker_str = retrieve_conf("broker")
    if (broker_str is None or len(broker_str.strip()) < 1):
        sys.exit("validate_configs(): Improper config")
    return 

def connect_kafka_producer():
    return KafkaProducer(bootstrap_servers=['localhost:9092'], api_version=(0, 10))

def post_to_kafka(producer):
    topics_dict = fakker_config.get("topics")
    for topic,dir in topics_dict.items():
        for curfile in glob.glob(dir + "/*"):
            with open(curfile, "r") as file:
                output_key = str(uuid.uuid1())
                key_bytes = bytes(output_key, encoding="utf-8")
                value_bytes = bytes(file.read(), encoding="utf-8")
                producer.send(k, key=key_bytes, value=value_bytes)
        print("test")


if (__name__ == "__main__"):
    init_logger()
    init_configs()
    validate_configs()
    producer = connect_kafka_producer()
    post_to_kafka(producer)



