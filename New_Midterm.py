import mraa
import time
import os
from gtts import gTTS
import configparser
from ciscosparkapi import CiscoSparkAPI
#config=configparser.ConfigParser()
#config.read('/home/root/ciscosapi.txt')
#print(str(config))
#apiKey = config['Token']['Key']
f=open("/home/root/ciscoapi.txt","r")
key=f.read()
start_loc=key.find("=")
end_loc=key.find("<txt>")
apiKey=key[start_loc+1:end_loc]
api=CiscoSparkAPI(access_token=apiKey)
roomName="edison"

pin=mraa.Aio(0)
humid=mraa.Aio(2)
pin.setBit(12)
humid.setBit(12)
#rawReading=pin.read()
f=open("rec2_command.txt","w")
f.write(" ")
f.close()


while True:
    try:
        f2=open("rec2_command.txt","r")
        string=f2.read()
        #print("string: "+string)
        if "temp" in string and "other" not in string:
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
        
        if "humidity" in string and "other" not in string:
            humReading=humid.read()
            volts=float(humReading / 819.0 ) 
            humidity= float( 100.0 / volts ) / float(5.0)
            response="The humidity is "+str(humidity)
            print(response)
            f=open("humid_to_be_sen.txt","w")
            f.write(response)
            f.close()
            os.system("scp humid_to_be_sen.txt root@10.0.0.19:/root/output.txt")
            print("humidity output file sent")
        if "other" in string and "room" in string:
            #api.messages.create(roomID,text="What's the temperature in the other room?")
            os.system("scp rec2_command.txt root@10.0.0.249:/home/root/command.txt")
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
