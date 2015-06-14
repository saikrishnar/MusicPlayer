                              
#!usr/env/python
import pyaudio
import wave
import os
CHUNK = 1024

	
folder = '/home/sirisha/Music'
os.chdir(folder)
files =  os.listdir(folder)
print files
for file in files:
     if file.endswith('.wav'):
	print file
	wf = wave.open(file, 'rb')
	#print (wf)
	p = pyaudio.PyAudio()
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(),output=True) 
	data = wf.readframes(CHUNK)
	while data != '':
      	      stream.write(data)
                             
if __name__ == "playlist":
	playlist()


