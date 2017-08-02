What does this software do?
	This software converts osu! beatmaps into light shows for Philips Hue lights.
	I am in no way affiliated with the organizations that own the trademarks, copyrights or whatever else for either osu! or Hue Personal Wireless Lighting.

I license this software under the MIT License (MIT), more info in LICENSE.txt

Steps to get this software working:

	0. This was developed on Windows 10 with Python 3.6.1 (Anaconda 4.4.0 64-bit), so attempting to run it on other platforms might not work so well

	1. Run Setup.py via python interpreter from the OsuToLights folder.

	2. Make sure GStreamer is installed into your path. (Or feel free to find some other way to play the audio, just subclass MusicPlayer.py and override the run function with a call to whatever program you'd like to use.)

	WARNING: This software creates a bunch of folders with somewhat nonsense names in the folder that you run it.

	NOTE: The programs you are meant to run are Infinite Light Show.py and Small Light Show.py (These are the files you will be wanting to execute) These will spam the terminal with the word Bang and output from GStreamer to help with light synchronization (Bang is supposed to happen at the same time the light changes color) Sometimes when you run the programs the lights start way too fast, so make sure that you run the program a couple of times before changing delays.

	3. Try using Infinite Light Show.py or Small Light Show.py, if you notice that your lights are significantly off beat, then it's time for some fun. If the lights simply do not trigger, then make sure your lights.py follows the sample provided in Sample lightspy.txt

	Getting the timing right:
		Open conf.txt
		If the music is starting before the lights:
			Raise the number in the last line
		If the music is starting after the lights:
			Lower the number in the last line OR raise the number in the 2nd line

		If the lights are going faster than the music:
			Lower the number in the 3rd line OR lower the number in the 4th line (4th line is used more than 3rd line, so it compounds the time difference faster)
		If the lights are going slower than the music:
			Raise the number in the 3rd line OR raise the number in the 4th line (same note as above).

		You'll eventually get it acceptably timed.
	4. That's it. Notes on how to customize this to your liking follow.


How the software works:
	The software is made up of 5 main component parts: The song finder (OsuFinder and CrazyOsuFinder), the light sequencer (CodeMaker and CrazyCodeMaker), the music player (MusicPlayer), the light sequence executor (CodeRunner), and the parts that actually work with the lights (lights(.py) and phue). phue is licensed under the MIT license copyright Nathanaël Lécaudé, more info in PHUE LICENSE file. When the 5 essential parts are stiched together in something like Small Light Show, they produce a light show. When I originally programmed this software, I found that the normal classes created too boring a light show, so I created the Crazy subclasses to liven it up a bit. They are what is used in Infinite Light Show and Small Light Show. If I did everything properly, Infinite Light Show and Small Light Show should work with any subclasses you create.

Do note that I use filenames and not class names here.

	OsuFinder:
		Used to find songs in the songsfolder, takes songsfolder location as input. It gets a "name" and a "codename" from CodeMaker which are used as input in other parts of the program. It should use CodeMaker to make the light sequence. 

	CodeMaker:
		Creates the directories for a song and its light sequence. Edit this if you want to change how things are sequenced in a big way. Takes "osuloc" and "alias" generated inside OsuFinder and outputs "codename" to OsuFinder. Does the heavy lifting.

	MusicPlayer:
		Takes "alias" which is "name" from OsuFinder. Has run(self) which should be made to play music.

	CodeRunner:
		Takes "codename" from OsuFinder. Runs the light sequence code generated in OsuFinder by CodeMaker.

	lights.py:
		The code run by CodeRunner uses this file to control how the lights switch. If you'd like to make minor changes to how the lights switch colors, do it here. Light color can be changed here. 

