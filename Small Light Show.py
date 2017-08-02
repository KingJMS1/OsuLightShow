from CrazyCodeMaker import CrazyCodeMaker
from CodeRunner import RunningThread
from MusicPlayer import MusicThread
import shutil
import os
import time

def sanitize(string):
    assert type(string) == str
    valids = 'abcdefghijklmnopqrstuvwxyzQWERTYUIOPASDFGHJKLZXCVBNM1234567890 '
    out = ""
    for c in string:
        if c in valids:
            out = out + c
    return out


try:
    config = open("conf.txt")
    songsfolder = config.readline().rstrip("\n")
except (FileNotFoundError, OSError):
    songsfolder = input("Please eneter your osu song directory (w/ a slash): ")
    config = open("conf.txt", 'w+')
    config.write(songsfolder)


alias = input("Song Name: ")
diff = input("Difficulty: ")

presongs = os.listdir(songsfolder)
songs = []
for x in presongs:
    try:
        int(x.split(" ")[0])
        songs.append(x)
    except BaseException:
        pass


for x in songs:     # Finds song by name
    if alias in sanitize(x) or alias.lower() in sanitize(x) or alias.upper() in sanitize(x):
        corrsong = x
        break

currfolder = songsfolder + corrsong + "\\"
diffs = [x for x in os.listdir(currfolder) if x[-1] == 'u']

for x in diffs:     #Finds difficulty by name
    if diff in sanitize(x):
        corrdiff = x
        break
try:
    newosu = currfolder + corrdiff
except NameError:
    print("Unable to find a difficulty by that name. ")
    print("Available difficulties are as follows: ")
    time.sleep(1)
    for x in diffs:
        print(x)
    print("\n")
    print("Will now throw an error to stop program.")
    time.sleep(1)
    raise AssertionError("Unable to find a difficulty by that name.")


name = alias
codeMaker = CrazyCodeMaker(newosu, name)
codeMaker.make_code()
madeFile = name + "\\" + name + ".py"
codename = codeMaker.codename
Music = MusicThread(alias)
RunCode = RunningThread(codename)
RunCode.start()
Music.start()
Music.join()
RunCode.join()