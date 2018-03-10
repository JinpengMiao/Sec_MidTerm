import mraa
import time
import os
from gtts import gTTS
pin=mraa.Aio(0)
pin.setBit(12)
#rawReading=pin.read()
f=open("rec2_command.txt","w")
f.write(" ")
f.close()
while True:
    try:
        f2=open("rec2_command.txt","r")
        string=f2.read()
        #print("string: "+string)
        if "temp" in string:
            rawReading=pin.read()
            volts=float(rawReading / 819.0)
            tempC= ( volts * 100 ) - 50
            tempF=(  tempC * 9.0 / 5.0 ) + 32.0
            response="The temperature is "+str(tempF)
            print(response)
            f=open("to_be_sent.txt","w")
            f.write(response)
            f.close()
            #tts=gTTS(text="The temperature is: "+str(tempF))
            #tts.save("to_be_sent.mp3")
            os.system("scp to_be_sent.txt root@10.0.0.19:/root/output.txt") 
            print("output file sent")
        else:
            pass
        f2.close()

    except ImportError:
        print("Error!!")
    f3=open("rec2_command.txt","r+")
    f3.truncate()
    f3.close()
    try:
        f4=open("to_be_sent.txt","r+")
        f4.truncate()
        f4.close()
    except IOError:
        pass

    time.sleep(5)
