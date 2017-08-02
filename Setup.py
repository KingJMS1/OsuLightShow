import os
import time
from phue import Bridge

print("We will now attempti to connect to your bridge, if this throws an exception, you probably need to press the sync button or make sure the IP is correct")
time.sleep(2)
bip = input("Please input the ipv4 address of your hue bridge: ")
Bridge = Bridge(bip)
try:
	os.remove("conf.txt")
	os.remove("lights.py")
except FileNotFoundError:
	pass

conf = open("conf.txt", "w+")
conf.write(input("Please input your osu song folder location ex. D:\Pgms2\osu!\Songs\ : ") + "\n")
conf.write(".16\n")
conf.write(".057\n")
conf.write(".062\n")
conf.write(".018\n")
conf.write("3.89\n")
conf.close()
lightfile = open("lights.py", 'w+')


lightfile.write("import phue\n")
lightfile.write("from phue import Bridge\n")
lightfile.write("\n")
lightfile.write('bridge = Bridge(' + "'" + bip + "'" + ')')
lightfile.write("\n")
lightfile.write('lts =' + input("Please input the names of the lights you would like to use (only tested with 3 lights) in the following format: ['<Light 1 name>', '<Light 2 name>', etc.]: "))
lightfile.write("\n")
lightfile.write("bri = " + input("Input the light brightness (1-254): ") + "\n")
lightfile.write('colorlist = [{"bri": bri, "sat": 250, "hue": 50500, "transitiontime": 0}, {"bri": bri, "sat": 250, "hue": 45400, "transitiontime": 0}, {"bri": bri, "sat": 250, "hue": 47100, "transitiontime": 0}, {"bri": bri, "sat": 250, "hue": 48600, "transitiontime": 0}, {"bri": bri, "sat": 250, "hue": 43000, "transitiontime": 0}]')
lightfile.write("\n")
lightfile.write("global current_color\n")
lightfile.write("global current_light\n")
lightfile.write("global lightdict\n")
lightfile.write("global next_color\n")
lightfile.write("lightdict = ")
lightfile.write(input("Write the order in which your lights should change in the following format: " + "{'<Light 1 name>': 0, '<Light 2 name>': 1, '<Light 3 name>': 2, etc.} : "))
lightfile.write("\n")
lightfile.write("current_color = 0\n")
lightfile.write("next_light = 0\n")
file = open("textdonttouch.txt")
for x in range(int(file.readline().rstrip("\n"))):
    lightfile.write(file.readline())
file.close()
lightfile.close()
print("Done, make sure you install gstreamer into your path")
time.sleep(4)