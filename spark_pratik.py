import os 
import mraa
import time
temp=mraa.Aio(0)
temp.setBit(12)
while True:
    if(os.path.isfile("/home/root/command.txt")==True):
        f=open("command.txt","r")
        command=f.read()
        if(len(command)>3):
            print("The command is: ")
            print(command)
            if "temp" in command:
                rawReading=temp.read()
                volts=float(rawReading / 819.0)
                tempC= ( volts * 100 ) - 50
                tempF=( tempC * 9.0 / 5.0 ) + 32.0
                response="The temperature is the other room is "+str(tempF)
                print(response)
                f=open("to_be_sent.txt","w")
                f.write(response)
                f.close()
                os.system("scp to_be_sent.txt root@10.0.0.19:/root/output.txt")
                f=open("to_be_sent.txt","r+")
                f.truncate()
                f.close()
                os.remove("to_be_sent.txt")

                print("output file sent")
            else:
                pass
        os.remove("command.txt")
    time.sleep(3)
