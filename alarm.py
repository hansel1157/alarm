import datetime
from playsound import playsound
import winsound
    
alarmHour = int(input("enter Hour : "))
alarmMin  = int(input("enter Minute : "))
alarmAm   = input(" am / pm : ")

if alarmAm == "pm":
    alarmHour += 12

while True:
    if alarmHour == datetime.datetime.now() .hour and alarmMin == datetime.datetime.now().minute:
        print("playing..")
        winsound.PlaySound("breach.wav", winsound.SND_LOOP + winsound.SND_ASYNC)
        val = input("this stop console closing. enter any key or text to exit : ")
        break
