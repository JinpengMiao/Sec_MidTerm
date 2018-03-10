#Python script that records user input and converts it to text.
#Makes use of "speech_recognition" and "pyaudio" modules.
#This script should be installed on a computer.
#The computer sends the text input to the Intel Edison via scp.
import pyttsx
import speech_recognition as sr
import os
from gtts import gTTS
import time
r = sr.Recognizer()

while True:
	with sr.Microphone() as source:
<<<<<<< HEAD
<<<<<<< HEAD
    		print ('Listening:')
		try:
    			audio = r.listen(source)
    			print ('Message heard')
=======
=======
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
    		print ('Say Something!')
		try:
    			audio = r.listen(source)
    			print ('Done!')
<<<<<<< HEAD
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
=======
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
                        text = r.recognize_google(audio)
                        print ("You Said: " + text)
                        try:
				f=open("command.txt","w")
                        	f.write(text)
                        	f.close()
                                tts=gTTS(text="Hello! You are sending the  message"+str(text), lang="en")
                                tts.save("good.mp3")
                                os.system("mpg123 good.mp3")     
			except:
				print("Can't create file")
		        print("\n About to send the file command.txt")
                        os.system("scp command.txt root@10.0.0.112:/home/root/rec2_command.txt") 
                        print("Mp3 file sent")
		except:
                        print("Didn't say anything")
		print("Yo\n\n")
<<<<<<< HEAD
<<<<<<< HEAD
	time.sleep(12)
=======
	time.sleep(5)
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
=======
	time.sleep(5)
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
