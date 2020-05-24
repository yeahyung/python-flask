from kafka import KafkaProducer
from json import dumps
import numpy as np
from time import sleep

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         key_serializer=None,
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

for _ in range(10):
    value = np.random.normal(loc = 10, scale=20, size=3).astype(str).tolist()
    values = ",".join(value)
    data = {'number' : values}
    producer.send('yeatest', key=b'my', value=data)
    sleep(0.1)
#asd = producer.send(topic='yeatest', value=b'Hello')
#qwe = producer.send(topic='yeatest', value=b'This is kafka python')
