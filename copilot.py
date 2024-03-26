from pythonosc import udp_client

# Set the IP address and port of the Ardour session's transport control
ardour_ip = "127.0.0.1"  # Replace with the actual IP address
ardour_port = 3819  # Replace with the actual port number

# Create an OSC client to send messages to the Ardour session
client = udp_client.SimpleUDPClient(ardour_ip, ardour_port)

# Start the transport
#client.send_message("/transport_play", 1)

# Stop the transport
client.send_message("/transport_stop", 1)