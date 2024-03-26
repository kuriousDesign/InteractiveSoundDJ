from pythonosc import udp_client
import time

class WaveformOscControl:
    def __init__(self, waveform_ip="127.0.0.1", port_to_waveform=8000):
        self.client = udp_client.SimpleUDPClient(waveform_ip, port_to_waveform)

    def start_transport(self):
        self.client.send_message("/1/play", 1)
        print("Transport started.")

    def stop_transport(self):
        self.client.send_message("/1/stop", 1)
        print("Transport stopped.")

    def mute_track(self, num):
        self.client.send_message("/1/mute/1/" + str(num), 1)
        print("Track " + str(num) + " muted.")

    def set_param(self, num, val):
        self.client.send_message("/param/" + str(num), val)
        print("Param " + str(num) + " with val: ." + str(val))

class AbletonOscControl:
    def __init__(self, waveform_ip = "127.0.0.1", port_to_ableton=11000):
        self.client = udp_client.SimpleUDPClient(waveform_ip, port_to_ableton)

    def start_transport(self):
        self.client.send_message("/live/song/start_playing", None)
        print("Transport started.")

    def stop_transport(self):
        self.client.send_message("/live/song/stop_playing", None)
        print("Transport stopped.")

    def mute_track(self, num):
        self.client.send_message("/live/track/" + str(num) + "/mute/" + str(num), None)
        print("Track " + str(num) + " muted.")

    def set_param(self, num, val):
        """this doesn't actually work yet"""
        self.client.send_message("/param/" + str(num) + str(val), None)
        print("Param " + str(num) + " with val: ." + str(val))


def main_ableton():
    target_ip = "127.0.0.1"
    port_to_ableton = 11000
    port_from_ableton = 11001
    client = AbletonOscControl(target_ip, port_to_ableton)
    client.start_transport()
    time.sleep(2)
    client.stop_transport()

def main_waveform():
    target_ip = "127.0.0.1"
    port_to_waveform = 8000
    client = WaveformOscControl(target_ip, port_to_waveform)
    client.start_transport()
    time.sleep(2)
    client.stop_transport()

if __name__ == "__main__":
    #main_ableton()
    main_waveform()

