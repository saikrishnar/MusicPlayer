                              
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
	
# Step 1: Instantiate the Pyaudio module
	p = pyaudio.PyAudio()
# Step 2: Open stream based on the wave object which has been input.
	stream = p.open(format=p.get_format_from_width(wf.getsampwidth()), channels=wf.getnchannels(), rate=wf.getframerate(),output=True) 
# Step 3:  read data from input file (based on the chunk size)
	data = wf.readframes(CHUNK)
# Step 4: Play stream (looping from beginning of file to the end)
	while data != '':
      	      stream.write(data)
              data = wf.readframes(CHUNK)
# Step 5: CLean the stuff up (Saving memory and RAM)
        stream.close() 
        p.terminate()
                             
if __name__ == "playlist":
	playlist()


