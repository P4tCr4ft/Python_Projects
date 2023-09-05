"""
Broadcast
"""

import pika

# Create a connection, say CN
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

# Create a channel in CN, say CH
channel = connection.channel()

# Create an Exchange
channel.exchange_declare(exchange="br_exchange", exchange_type="fanout")

for i in range(4):
    message = "Hello! " + str(i)
    # Publish the message
    channel.basic_publish(exchange="br_exchange", routing_key="", body=message)
    print(f"[x] Sent message: {message}")

# Delete the Exchange
# If 'if_unused' is set to True, then Exchange is deleted only if there are
# no queues associated with the exchange. But set to False, it will delete
# the Exchange regardless of any associated queues.
channel.exchange_delete(exchange="br_exchange", if_unused=False)

# Close the connection, automatically closes the channel
connection.close()
