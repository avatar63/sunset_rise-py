import os                       #allows us to use the entire os library and interact with the command line which we are using to influence the wallpaper
import requests                 #allows us to pull the API necessary to know the time of sunset and sunrise
import json                     #allows us to read information in the json file extracted
from time import strftime       #allows us to select current time used to compare it with time of sunset/rise 
import random                   #used for selecting a random file from the list of files.

print(os.system("/usr/bin/gsettings get org.gnome.desktop.background picture-uri"))
r = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400")

data=json.loads(r.content.decode())

sun_rise=data["results"]["sunrise"]
sun_set=data["results"]["sunset"]

print("Sunrise", sun_rise)
print("Sunset",sun_set)

c_time= strftime("%H:%M:%S %p")

time = str(c_time)

print(c_time)
filename = str(random.randrange(0,2))
c_file = "wp"+filename
print(c_file)

if c_time==sun_rise:
    print("/usr/bin/gsettings set org.gnome.desktop.background picture-uri ~/scripts/"+c_file+"/sunrise.jpg")
elif c_time==sun_set:
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri ~/scripts/"+c_file+"/sunrise.jpg")