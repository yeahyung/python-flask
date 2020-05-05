import json
import socket
import sys
from kafka import KafkaConsumer

consumer = KafkaConsumer("mytest", bootstrap_servers=["localhost:9092"],
                         group_id="my-group")


address = "localhost"
port = 5044

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("socket created")
try:
   s.connect((address, port))
   print("socket connected")

   for message in consumer:
       message = message.value
       print(message)
       s.sendall(message)
       s.send("\n".encode())
except socket.error as msg:
   print("connection refused", msg)
s.close()
exit()