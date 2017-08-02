from CrazyOsuFinder import CrazySearchingMakingThread
from MusicPlayer import MusicThread
from CodeRunner import RunningThread

# SearchingMakingThread songsfolder with slash. It searches for an osu file to convert. After running, it stores new fileloc (alias) as self.name and codename as self.codename
# MusicThread takes alias and plays the music.
# RunningThread takes codename and runs the code.

try:
    config = open("conf.txt")
    songsfolder = config.readline().rstrip("\n")
except (FileNotFoundError, OSError):
    raise AssertionError("Config doesn't seem to be set up correctly")

while True:
    acquireplz = CrazySearchingMakingThread(songsfolder)
    acquireplz.start()
    acquireplz.join()
    alias = acquireplz.name
    codename = acquireplz.codename
    Music = MusicThread(alias)
    RunCode = RunningThread(codename)
    RunCode.start()
    Music.start()
    RunCode.join()
    Music.join()