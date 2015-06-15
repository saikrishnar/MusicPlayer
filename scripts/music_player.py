#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import pyaudio
import wave
import os
import time,threading, multiprocessing
from subprocess import check_call
flag = 0

p = pyaudio.PyAudio()
def play_file(flag,count):
	#CHUNK = 512 
        
      print flag
      print 'count is ' + str(count)
      folder = '/home/sirisha/Music'
      os.chdir(folder)
      files =  os.listdir(folder)
        #flag = 0
      if flag == 0: 
	#print files
        wav_array = []
	for file in files:
            
  	    if file.endswith('.wav'):
                wav_array.append(file)
                #print file
        file = wav_array[count]         
        wf = wave.open(file, 'rb')
    
    	# Step 1: Instantiate the Pyaudio module
                

        # define callback (1.2)
        def callback(in_data, frame_count, time_info, status):
                       data = wf.readframes(frame_count)
                       return (data, pyaudio.paContinue)

  	# Step 2: Open stream based on the wave object which has been input.
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
        channels=wf.getnchannels(),
        rate=wf.getframerate(),
        output=True,
        stream_callback=callback)
    	
    	# Step 4: Play stream (looping from beginning of file to the end)
                #if  flag == 0:
        stream.start_stream()
                #else:
      else:
            p.terminate()
            #p = pyaudio.PyAudio()                        
                   
   	# Step 5: Clean the stuff up (Saving memory and RAM)
   	         #   stream.stop_stream() 
                 #   stream.close()
    	         #   p.terminate()
   	 

class Example(QtGui.QMainWindow):
    
	def __init__(self):
    	    super(Example, self).__init__()
            
   	    self.initUI()

	def setColor(self, color):
    	    self.color = QtGui.QColor(800800)
    	    self.update()


   	 
	def initUI(self): 
            
    	    btn1 = QtGui.QPushButton("Play", self)
    	    btn1.resize(btn1.sizeHint())
            btn1.move(50, 30)

    	    btn2 = QtGui.QPushButton("Stop", self)
    	    btn2.resize(btn2.sizeHint())
            btn2.move(150, 30)

            btn3 = QtGui.QPushButton("Next", self)
            btn3.resize(btn3.sizeHint())
            btn3.move(250, 30)
 	 
    	    btn4 = QtGui.QPushButton("Exit", self)
            btn4.resize(btn3.sizeHint())
            btn4.move(350, 30)
     
            
            count = 0
            btn1.clicked.connect(lambda: self.buttonClicked(count))       	 
    	    btn2.clicked.connect(lambda: self.buttonClicked(count))
            btn3.clicked.connect(lambda: self.buttonClicked(count))
            btn4.clicked.connect(QtCore.QCoreApplication.instance().quit)

    	    self.statusBar()
   	 
    	    self.setGeometry(300, 300, 500, 150)
    	    self.setWindowTitle('Simple Music Player')
    	    self.show()

  	 
	def buttonClicked(self, count):          
    	   sender = self.sender()
           #print sender
           
           
    	   if sender.text() == 'Play':
         	self.statusBar().showMessage('Yipee')
                flag = 0
                
                p = pyaudio.PyAudio()
                #t = multiprocessing.Process(target=play_file())
                #t1.daemon = False
                #threads.append(t)
                #t.start()
         	play_file(flag,count)

           elif sender.text() == 'Stop':
                 flag = 1
                 
                 self.statusBar().showMessage('Stopping :(')
                 #t2 = threading.Thread(target=play_file(flag))
                 play_file(flag, count) 

           elif sender.text() == 'Next':
                self.statusBar().showMessage('Yipee')
                flag = 0
                count = count + 1
                p = pyaudio.PyAudio()
                #t = multiprocessing.Process(target=play_file())
                #t1.daemon = False
                #threads.append(t)
                #t.start()
         	play_file(flag,count)      	 
    	   else:
         	self.statusBar().showMessage(sender.text() + ' was pressed')
     	        stream.stop_stream()
    
def main():
        
	app = QtGui.QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())


if __name__ == '__main__':

	main()



