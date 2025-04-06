import redis

# Connect to Redis server
r = redis.Redis(host='localhost', port=6380, db=0)

# Channel names
ping_channel = 'ping-channel'
pong_channel = 'pong-channel'

# Subscribe to the ping channel to receive ping messages
pubsub = r.pubsub()
pubsub.subscribe(ping_channel)

print("Listening for ping messages...")

for message in pubsub.listen():
    if message['type'] == 'message':
        ping_message = message['data'].decode('utf-8')
        print(f"Received: {ping_message}")

        # Extract the ping counter value
        ping_counter = ping_message.split()[1]

        # Publish the pong message to the pong channel
        pong_message = f"pong {ping_counter}"
        r.publish(pong_channel, pong_message)
        print(f"Sent: {pong_message}")
