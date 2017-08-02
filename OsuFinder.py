import threading
import os
import time
import CodeMaker
import random

class SearchingMakingThread(threading.Thread):
    def __init__(self, songsfolder):
        threading.Thread.__init__(self, target=self.run)
        self.name = None
        self.songsfolder = songsfolder
        presongs = os.listdir(songsfolder)
        self.songs = []
        for x in presongs:
            try:
                int(x.split(" ")[0])
                self.songs.append(x)
            except BaseException:
                pass
    
    def run(self):
        next_target = random.choice(self.songs)
        currfolder = self.songsfolder + next_target + "\\"
        newosu = random.choice([x for x in os.listdir(currfolder) if x[-1] == 'u'])
        self.name = newosu[0:3] + currfolder[-4:-2]
        nwfile = currfolder + newosu
        codeMaker = CodeMaker.CodeMaker(nwfile, self.name)
        codeMaker.make_code()
        self.madeFile = self.name + "\\" + self.name + ".py"
        self.codename = codeMaker.codename