import mraa
import time
import os
from gtts import gTTS
import smtplib
from email.mime.text import MIMEText
temp_dict={
        "low":30,
        "high":71
}

pin=mraa.Aio(1)
pin.setBit(12)
led=mraa.Gpio(13)
led.dir(mraa.DIR_OUT)
led.write(0)
led_2=mraa.Gpio(7)
led_2.dir(mraa.DIR_OUT)
led_3=mraa.Gpio(12)
led_3.dir(mraa.DIR_OUT)
while True:
    led.write(0)
    time.sleep(2)
    rawReading=pin.read()
    print("RawReading :"+str(rawReading))
    volts=float(rawReading / 819.0 )
    print("Volts is:"+str(volts))
    tempC=( volts * 100 ) - 50
    print("TempC is: "+str(tempC))
    tempF=( tempC * 9.0  / 5.0 ) + 32.0 
    print("Temperature is: "+str(tempF))
    led.write(0)
    led_2.write(0)
    led_3.write(0)
    if(float(tempF) < float(temp_dict["low"]) or float(tempF) > float(temp_dict["high"])):
        for i in range(1,3):
            led.write(1)
            time.sleep(0.5)
            led_2.write(1)
            time.sleep(0.5)
            led_3.write(1)
            time.sleep(0.5)
            led.write(0)
            time.sleep(0.5)
            led_2.write(0)
            time.sleep(0.5)
            led_3.write(0)

        print("Warning! Temperature outside range!!")
        content="Warning! The temperature is outside the safe range."
        mail=smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("secure.embedded2018@gmail.com","itpsecurity")
        mail.sendmail("secure.embedded2018@gmail.com","sampy.prithvi@gmail.com",content)

        mail.close()
        file_content="Warning! The temperature is outside the range"
        f=open("warning.txt","w")
        f.write(file_content)
        f.close()
        os.system("scp warning.txt root@192.168.20.182:/root/warning_1.txt")
        os.remove("warning.txt")
    time.sleep(5)

