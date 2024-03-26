from pythonosc import udp_client

# Set up OSC client
client = udp_client.SimpleUDPClient("127.0.0.1", 3819)  # Replace with Ardour's OSC port

# Define OSC address and value for the reverb parameter
osc_address = "/path/to/reverb/parameter"
new_value = 0.5  # Example value

# Send OSC message to Ardour
client.send_message(osc_address, new_value)
