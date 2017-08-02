import threading
import subprocess
import time

class RunningThread(threading.Thread):
    def __init__(self, codename):
        threading.Thread.__init__(self, target=self.run)
        self.codename = codename
    
    def run(self):
        subprocess.run(["python", self.codename])