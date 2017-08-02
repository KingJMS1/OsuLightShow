import threading
import subprocess
import time

class MusicThread(threading.Thread):
    def __init__(self, alias):
        threading.Thread.__init__(self, target=self.run)
        self.name = alias
        conf = open("conf.txt")
        for x in range(5):
            conf.readline()
        self.delay5 = float(conf.readline().rstrip("\n"))
    
    def run(self):
        time.sleep(self.delay5)
        subprocess.call(["gst-play-1.0", self.name + '/audio.mp3'], shell=True)