# fakker
Testing tool to ease the developer into posting messages to kafka from a directory and a configured set of topics.

### Startup

Grab a Docker compose yaml that includes Kafka and Zookeeper.

```
% docker-compose up
```

```
python3 fakker.py
```
Executes the program and posts the messages to the configured topics

![image](https://github.com/aboodmm/fakker/assets/2085511/d060d7f5-f6a2-4d2e-b248-17c4b7742620)
