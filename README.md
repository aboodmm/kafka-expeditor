# fakker
Eliminate the extremely painful labor of posting to kafka for manual testing


### Startup

```
% docker-compose up
```
This will start the included Kafka and Zookeeper bundle.

```
python3 fakker.py
```
Executes the program and posts the messages to the configured topics
