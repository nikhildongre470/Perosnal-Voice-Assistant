import os
import eel
import pyttsx3

from engine.features import *
from engine.command import *
eel.init("www")

playAssistantSound()

os.system('start msedge.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)




