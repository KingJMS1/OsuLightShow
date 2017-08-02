import os
import shutil

class CodeMaker(object):
    def __init__(self, osuloc, alias):
        self.osu = open(osuloc, encoding="utf8")
        self.osufolder = "\\".join(osuloc.split("\\")[0:-1])
        self.name = alias
        try:
            os.mkdir(self.name)
        except FileExistsError:
            shutil.rmtree(self.name)
            os.mkdir(self.name)
        self.codename = self.name + "/" + self.name + ".py"
        self.audioout = self.name + "/" + "audio.mp3"
        self.code = open(self.name + "/" + self.name + ".py", 'w+')
        shutil.copy("lights.py", self.name + "/" + "lights.py")
        shutil.copy("phue.py", self.name + "/" + "phue.py")
        self.osu.readline()
        self.osu.readline()
        self.osu.readline()
        self.afile = self.osu.readline().rstrip("\n").split(":")[1][1:]
        self.afile = self.osufolder + "\\" + self.afile
        shutil.copy(self.afile, self.audioout)
        conf = open("conf.txt")
        conf.readline()
        self.delay1 = float(conf.readline().rstrip("\n"))
        self.delay2 = float(conf.readline().rstrip("\n"))
        self.delay3 = float(conf.readline().rstrip("\n"))
        self.delay4 = float(conf.readline().rstrip("\n"))
        
    def make_code(self):
        HitObjectFound = False
        
        while not HitObjectFound:
            line = self.osu.readline().rstrip("\n")
            if line == '[HitObjects]':
                HitObjectFound = True
        
        self.code.write("import time\n")
        self.code.write("import lights\n")
        self.code.write("\n")
        
        EofFound = False
        
        comboStarters = [5, 6, 12]
        
        prevtime = 0
        
        while not EofFound:
            hitobj = self.osu.readline().rstrip("\n").split(",")
            try:
                timee = int(hitobj[2])
                combo = int(hitobj[3])
                if combo in comboStarters:
                    if prevtime == 0:
                        self.code.write("print('3')\n")
                        self.code.write("time.sleep(" + str(2) + ")\n")
                        self.code.write("print('2')\n")
                        self.code.write("time.sleep(" + str(2) + ")\n")
                        self.code.write("print('1')\n")
                        self.code.write("time.sleep(" + str(((timee - prevtime)/1000) + self.delay1) + ")\n")
                        self.code.write("lights.next()\n")
                        prevtime = timee                    
                    else:
                        if timee >= 50:
                            self.code.write("time.sleep(" + str(((timee - prevtime)/1000)-self.delay2) + ")\n")
                            self.code.write("lights.next()\n")
                            self.code.write("print('Bang')\n")
                            prevtime = timee
                        else:
                            self.code.write("time.sleep(" + str(((timee - prevtime)/1000)) + ")\n")
                            self.code.write("lights.next()\n")
                            self.code.write("print('Bang')\n")
                            prevtime = timee                    
            except IndexError:
                EofFound = True
        self.osu.close()
        self.code.close()
        