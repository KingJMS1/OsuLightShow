import os
import shutil
from CodeMaker import CodeMaker

class CrazyCodeMaker(CodeMaker):
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
        comboStarters = [5,6,12]
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
                        self.code.write("lights.combo()\n")
                        prevtime = timee                    
                    else:
                        if timee-prevtime >= 62:
                            self.code.write("time.sleep(" + str(((timee - prevtime)/1000)-self.delay3) + ")\n")
                            self.code.write("lights.combo()\n")
                            self.code.write("print('Bang')\n")
                            prevtime = timee
                        else:
                            self.code.write("time.sleep(" + str(((timee - prevtime)/1000)) + ")\n")
                            self.code.write("lights.combo()\n")
                            self.code.write("print('Bang')\n")
                            prevtime = timee
                else:
                    if prevtime == 0:
                        self.code.write("print('3')\n")
                        self.code.write("time.sleep(" + str(2) + ")\n")
                        self.code.write("print('2')\n")
                        self.code.write("time.sleep(" + str(2) + ")\n")
                        self.code.write("print('1')\n")
                        self.code.write("time.sleep(" + str(((timee - prevtime)/1000) + self.delay1) + ")\n")
                        self.code.write("lights.cycle()\n")
                        prevtime = timee
                    else:
                        if timee - prevtime >= 18:
                            self.code.write("time.sleep(" + str(((timee - prevtime)/1000)-self.delay4) + ")\n")
                            self.code.write("lights.cycle()\n")
                            self.code.write("print('Bang')\n")
                            prevtime = timee
                        else:
                            self.code.write("time.sleep(" + str(((timee - prevtime)/1000)) + ")\n")
                            self.code.write("lights.cycle()\n")
                            self.code.write("print('Bang')\n")
                            prevtime = timee
            except IndexError:
                EofFound = True
        self.osu.close()
        self.code.close()        