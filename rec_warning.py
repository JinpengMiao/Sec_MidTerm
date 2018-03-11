import os
from gtts import gTTS
while True:
    response=""
    if(os.path.isfile("/root/warning_1.txt")==True):
        f=open("warning_1.txt","r")
	response=f.read()
	if(len(response)>3):
	    print("length of response:"+str(len(response)))
	    print("response: "+response)
            tts=gTTS(text=response, lang="en")
            if(len(response)>3):
		tts.save("/root/warning_1.mp3")
    		os.system("mpg123 /root/warning_1.mp3")
                response=""
		f.close()
		f=open("warning_1.txt","r+")
		f.truncate()
		f.close()
        	if(os.path.isfile("/root/warning_1.mp3")==True):
               	    f=open("warning_1.mp3","r+")
            	    f.truncate()
            	    f.close()
            	    os.remove("/root/warning_1.mp3")

	
