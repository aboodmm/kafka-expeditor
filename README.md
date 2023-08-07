# fakker
Eliminate the extremely painful labor of posting to kafka for manual testing


### Configuration

add the following to your login script

```
alias zookup='<path_to_kafka>/bin/zookeeper-server-start.sh <path_to_kafka>/config/zookeeper.properties'
alias kafkaup='<path_to_kafka>/bin/kafka-server-start.sh <path_to_kafka>/config/server.properties'
```
