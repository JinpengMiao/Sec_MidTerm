import mraa
import time
import os
from gtts import gTTS
import configparser
from ciscosparkapi import CiscoSparkAPI
import sqlite3
import re
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
f=open("rec2_command.txt","w")
f.write(" ")
f.close()
try:
    print("0")
    db=sqlite3.connect('midterm.db')
    db.row_factory=sqlite3.Row
    print("1")
    cursor=db.cursor()
    #print("2")
    
    #cursor.execute("CREATE TABLE IF NOT EXISTS tempLimit(id INTERGER PRIMARY KEY, lowerLimit REAL, upperLimit REAL)")
    #print("3")
    #db.commit()
    #cursor.execute("INSERT INTO tempLimit VALUES(72,30)")
    #db.commit()
    #print("4")
    #cursor.execute("CREATE TABLE IF NOT EXISTS humidLimit(id INTERGER PRIMARY KEY, lowerLimit REAL, upperLimit REAL)")
    #print("5")
    #db.commit()
    #cursor.execute("INSERT INTO humidLimit VALUES(40,20)")
    print("Hello here")
    #db.commit()
except:
    pass

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
            response="The temperature is "+str(tempF)+" Fahrenheit"
            print(response)
            f=open("to_be_sent.txt","w")
            f.write(response)
            f.close()
            #tts=gTTS(text="The temperature is: "+str(tempF))
            #tts.save("to_be_sent.mp3")
            os.system("scp to_be_sent.txt root@192.168.20.182:/root/output.txt") 
            print("output file sent")
        
        if "humidity" in string and "other" not in string:
            humReading=humid.read()
            volts=float(humReading / 819.0 ) 
            humidity= float( 100.0 / volts ) / float(5.0)
            response="The humidity is "+str(humidity +" percent")
            print(response)
            f=open("humid_to_be_sen.txt","w")
            f.write(response)
            f.close()
            os.system("scp humid_to_be_sen.txt root@192.168.20.182:/root/output.txt")
            print("humidity output file sent")
        if "other" in string and "room" in string:
            print("string: "+ string)
            #api.messages.create(roomID,text="What's the temperature in the other room?")
            os.system("scp rec2_command.txt root@192.168.20.86:/home/root/command.txt")
        if (len(string)>5 and "humidity" not in string and "other" not in string and "temp" not in string and "change" not in string and "lower" not in string and "upper" not in string):

            response="I'm sorry.  I don't have a reasonable response for that"
            f=open("invalid.txt","w")
            f.write(response)
            f.close()
            os.system("scp invalid.txt root@192.168.20.182:/root/output.txt")
            os.remove("invalid.txt")
        if("change" in string and "lower" in string and "temp" in string):
            print("string is:")
            print(string)
            newLower=re.findall("\d+",string)[0]
            #[float(s) for s in string.split(" ") if s.isdigit()]
            #newLower=s[0]
            print("New Lower Temperature and its type: "+str(newLower)+ "  "+str(type(newLower)))
            #cursor.execute("SELECT upperLimit from tempLimit where id=1")
            #oldUpper=cursor.fetchone()
            query="UPDATE tempLimit SET lowerLimit="+str(newLower)
            cursor.execute(query)
            db.commit()

            '''if(float(newLower) > float(oldUpper[0])):
                print("Cannot have a higher lower-limit than the upper-limit")
            else:
                cursor.execute("UPDATE tempLimit SET lowerLimit = ? where id = 1",(newLower))
               '''
            print("The new lower limit has been set")
        if("change" in string and "upper" in string and "temp" in string):
            print("string is: "+string)
            #[float(s) for s in string.split(" ") if s.isdigit()]
            #newUpper=s[0]
            newUpper=re.findall("\d+",string)[0]
            print("NewUpper limit is:"+str(newUpper))
            query="UPDATE tempLimit SET upperLimit="+str(newUpper)
            cursor.execute(query)
            db.commit()
            print("Changed upper-limit successfully")
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
