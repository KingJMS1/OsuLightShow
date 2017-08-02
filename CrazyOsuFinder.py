import threading
import os
import time
import CrazyCodeMaker
import random
from OsuFinder import SearchingMakingThread

class CrazySearchingMakingThread(SearchingMakingThread):
    def run(self):
        next_target = random.choice(self.songs)
        currfolder = self.songsfolder + next_target + "\\"
        newosu = random.choice([x for x in os.listdir(currfolder) if x[-1] == 'u'])
        self.name = newosu[0:3] + currfolder[-4:-2]
        nwfile = currfolder + newosu
        codeMaker = CrazyCodeMaker.CrazyCodeMaker(nwfile, self.name)
        codeMaker.make_code()
        self.madeFile = self.name + "\\" + self.name + ".py"
        self.codename = codeMaker.codename