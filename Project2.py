import tkinter as tk
from tkinter import font
import requests

def get_weather(city):
    weather_key = '637aca5742a48d6342124c656ac9d506'
    url = 'http://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather_responce = response.json()
    name = weather_responce['city']['name']
    country = weather_responce['city']['country']
    #print(name)
    desc = weather_responce['list'][0]['weather'][0]['description']
    #print(desc)
    temprature = weather_responce['list'][0]['main']['temp'] 
    feels_like = weather_responce['list'][0]['main']['feels_like']
    humidity = weather_responce['list'][0]['main']['humidity']
    population = weather_responce['city']['population']
     
    #print(temprature)
    try:
        final_string = 'City: %s \nCountry: %s \nConditions: %s \nTemprature (*F): %s \nFeels like: %s \nHumidity: %s \nPopulation: %s' % (
            name,country, desc, temprature,feels_like,humidity, population)
    except:
        final_string = 'Problem retriving weather information'
    lable['text'] = final_string

root = tk.Tk()

canvas = tk.Canvas(root,bg="#80b3ff",height=500,width=600 )
canvas.pack(fill="both",expand=True)

backgroup_image = tk.PhotoImage(
    file='C:/Users/nitinswa/Desktop/Project2VBC/Color-Paint-Art-Background-PNG.png')
backgroup_lable = tk.Label (root, image=backgroup_image)
backgroup_lable.place(relwidth=1,relheight=1)


frame = tk.Frame(root,bg="#1aff1a", bd=5)
frame.place(rely=0.1,relx=0.5,relheight=0.1,relwidth=0.75, anchor="n")

entry = tk.Entry(frame, font=('Courier',15,'bold'))
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame, text="Get Weather",font=40,bg='Orange', command= lambda: get_weather(entry.get()))
button.place(relx=0.7,relheight=1,relwidth=0.3)

lower_frame = tk.Frame(root,bg="#1aff1a", bd=10)
lower_frame.place(rely=0.25,relx=0.5,relheight=0.6,relwidth=0.75, anchor="n")


#button.pack(side="left",fill="x",expand=True)
lable = tk.Label(lower_frame,bg="#1aff1a",font=('Courier',15,'bold'),anchor='nw',bd=4,justify='left')
lable.place(relwidth=1,relheight=1)


lablesignature = tk.Label(lower_frame,bg="#1aff1a",font=('Courier',15,'bold'),anchor='s',justify='left')
lablesignature.place(relx=0,rely=0.9)
lablesignature['text'] = "Created by Nitin Swarup"

root.mainloop()

#637aca5742a48d6342124c656ac9d506
#pro.openweathermap.org/data/2.5/forecast/hourly?lat={lat}&lon={lon}&appid={your api key}