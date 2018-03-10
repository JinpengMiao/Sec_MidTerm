import os
from gtts import gTTS
while True:
<<<<<<< HEAD
<<<<<<< HEAD
    response=""
    if(os.path.isfile("/root/output.txt")==True):
        f=open("output.txt","r")
	response=f.read()
	if(len(response)>3):
	    print("length of response:"+str(len(response)))
	    print("response: "+response)
            tts=gTTS(text=response, lang="en")
            if(len(response)>3):
		tts.save("/root/output.mp3")
    		os.system("mpg123 /root/output.mp3")
                response=""
		f.close()
		f=open("output.txt","r+")
		f.truncate()
		f.close()
        	if(os.path.isfile("/root/output.mp3")==True):
               	    f=open("output.mp3","r+")
            	    f.truncate()
            	    f.close()
            	    os.remove("/root/output.mp3")

	
=======
=======
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
    if(os.path. isfile("/root/output.txt")==True):
        f=open("output.txt","r")
        response=f.read()
        if(response!=""):
            tts=gTTS(text=response, lang="en")
            tts.save("output.mp3")
            os.system("mpg123 output.mp3")

	f.close()
	f=open("output.txt","r+")
	f.truncate()
	f.close()
<<<<<<< HEAD
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
=======
>>>>>>> d1dcd1996cfe2aaeae11043b233834b5d38c3887
