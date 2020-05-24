from kafka import KafkaConsumer

consumer = KafkaConsumer("yeatest", bootstrap_servers=["localhost:9092"],
                         group_id="my-group")


for msg in consumer:
    print(msg)