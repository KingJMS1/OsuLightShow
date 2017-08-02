import sys
import subprocess
import pygame
import time
import os
import shutil
import threading
import random

global codename
global name
global songsfolder


global songsfolder
global name

osufile = input("Osu file location? ")
osu = open(osufile, encoding="utf8")
osufolder = osufile.split("\\")[0:-1]
osufolder = "\\".join(osufolder)
name = input("What should it be called? ")

songsfolder = "\\".join(osufolder.split("\\")[0:-1]) + "\\"

try:
    os.mkdir(name)
except FileExistsError:
    shutil.rmtree(name)
    os.mkdir(name)
print("Worked")
codename = name + "/" + name + ".py"
code = open(name + "/" + name + ".py", 'w+')
# afile = input("Audio file location? ")
audioout = name + "/" + "audio.mp3"
# subprocess.run(["ffmpeg", "-i", afile, audioout])
shutil.copy("lights.py", name + "/" + "lights.py")
shutil.copy("phue.py", name + "/" + "phue.py")

osu.readline()
osu.readline()
osu.readline()

afile = osu.readline().rstrip("\n").split(":")[1][1:]
afile = osufolder + "\\" + afile
shutil.copy(afile, name + "/" + "audio.mp3")


HitObjectFound = False

while not HitObjectFound:
    line = osu.readline().rstrip("\n")
    if line == '[HitObjects]':
        HitObjectFound = True

code.write("import time\n")
code.write("import lights\n")
code.write("\n")

EofFound = False

comboStarters = [5, 6, 12]

prevtime = 0

while not EofFound:
    hitobj = osu.readline().rstrip("\n").split(",")
    try:
        timee = int(hitobj[2])
        combo = int(hitobj[3])
        if combo in comboStarters:
            if prevtime == 0:
                code.write("print('3')\n")
                code.write("time.sleep(" + str(2) + ")\n")
                code.write("print('2')\n")
                code.write("time.sleep(" + str(2) + ")\n")
                code.write("print('1')\n")
                code.write("time.sleep(" + str(2) + ")\n")
                code.write("print('Go')\n")
                code.write("time.sleep(" + str(((timee - prevtime)/1000) + .16) + ")\n")
                code.write("lights.next()\n")
                prevtime = timee                    
            else:
                if timee >= 50:
                    code.write("time.sleep(" + str(((timee - prevtime)/1000)-.0572) + ")\n")
                    code.write("lights.next()\n")
                    code.write("print('Bang')\n")
                    prevtime = timee
                else:
                    code.write("time.sleep(" + str(((timee - prevtime)/1000)) + ")\n")
                    code.write("lights.next()\n")
                    code.write("print('Bang')\n")
                    prevtime = timee                    
    except IndexError:
        EofFound = True
osu.close()
code.close()


def thread1():
    global codename
    subprocess.run(["python", codename])
def thread2():
    global name
    time.sleep(5.89)
    subprocess.call(["gst-play-1.0", name + '/audio.mp3'], shell=True)


        
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

def thread3():
    listofsongs = os.listdir(songsfolder)
    global codename
    global name
    global t1
    global t2
    actualist = []
    for x in listofsongs:
        try:
            int(x.split(" ")[0])
            actualist.append(x)
        except BaseException:
            pass
    while True:
        time.sleep(15)
        next_target = random.choice(actualist)
        currfolder = songsfolder + next_target + "\\"
        newosu = random.choice([x for x in os.listdir(currfolder) if x[-1] == 'u'])
        name = newosu[0:3] + currfolder[-4:-2]
        nwfile = currfolder + newosu
        makecode(osufile=nwfile, names=name)
        t1.join()
        t2.join()
        t1 = threading.Thread(target=thread1)
        t2 = threading.Thread(target=thread2)
        t1.start()
        t2.start()



t1.start()
t2.start()