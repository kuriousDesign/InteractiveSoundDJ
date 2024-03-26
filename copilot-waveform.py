from pythonosc import udp_client

# Set the IP address and port of the Waveform Free 12 application
ip_address = "127.0.0.1"
port = 8000

# Create an OSC client
client = udp_client.SimpleUDPClient(ip_address, port)

# Send an OSC message to start the song
client.send_message("/1/stop", 1)

# Wait for some time (e.g., 5 seconds)
# ...

# Send an OSC message to stop the song
# client.send_message("/stop", 1)