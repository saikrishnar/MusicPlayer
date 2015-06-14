#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
from PyQt4 import QtGui, QtCore
import pyaudio
import wave
import os


class Example(QtGui.QMainWindow):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):      

        btn1 = QtGui.QPushButton("Play", self)
        btn1.move(30, 50)

        btn2 = QtGui.QPushButton("Stop", self)
        btn2.move(150, 50)
      
        btn1.clicked.connect(self.buttonClicked)            
        btn2.clicked.connect(self.buttonClicked)
        
        self.statusBar()
        
        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Simple Music Player')
        self.show()
        
    def buttonClicked(self):
      
        sender = self.sender()
        if sender.text() == 'Play':
             self.statusBar().showMessage('Yipee')
             play_list()
             
        else:
             self.statusBar().showMessage(sender.text() + ' was pressed')

def play_list():
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
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
