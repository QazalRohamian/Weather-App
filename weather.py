import tkinter as tk
from tkinter import messagebox
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def get_weather():
    try:
        city = textfield.get()
        geolocator = Nominatim(user_agent="geopiExercises")
        location = geolocator.geocode(city)
        lat = location.latitude
        lng = location.longitude
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=lng, lat=lat)
        city_lable.config(text=result.split("/")[1])
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        time_lable.config(text="LOCAL TIME")

        api_key = "80df2570fcc0457a598b5eff14b1ea20"
        api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lng}&appid={api_key}"

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"]-273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        temp_lable.config(text=f"{temp} °")
        condition_lable.config(text=f"{condition} | FEELS LIKE {temp} °")
        wind_lable.config(text=wind)
        humidity_lable.config(text=humidity)
        description_lable.config(text=description)
        pressure_lable.config(text=pressure)

    except Exception as error:
        print(error)
        messagebox.showerror("Weather App", "Invalid Entry")
   



win = tk.Tk()
win.title("weather app")
win.geometry("900x500+300+200")
win.resizable(False, False)


search_image = tk.PhotoImage(file="search.png")
search_image_lable = tk.Label(win, image=search_image)
search_image_lable.pack(side=tk.TOP, pady=20)

textfield = tk.Entry(win, justify="center", width=17, font=("poppins", 20, "bold"), bg="#404040", fg="white", border=0)
textfield.place(x=280, y=40)

search_icon = tk.PhotoImage(file="search_icon.png")
search_icon_button = tk.Button(win, image=search_icon, border=0, cursor="hand2", bg="#404040", command=get_weather)
search_icon_button.place(x=590, y=34)

logo_image = tk.PhotoImage(file="logo.png")
logo_image_labl = tk.Label(win, image=logo_image)
logo_image_labl.pack(side=tk.TOP)

box_image = tk.PhotoImage(file="box.png")
box_image_lable = tk.Label(win, image=box_image)
box_image_lable.pack(pady=10, side=tk.BOTTOM)

city_lable = tk.Label(win, font=("arial", 40, "bold"), fg="#e355cd")
city_lable.place(x=120, y=160)

time_lable = tk.Label(win, font=("arial", 20, "bold"), fg="#4b4bcc")
time_lable.place(x=120, y=230)

clock = tk.Label(win, font=("Helvetica", 20, "bold"), fg="#4b4bcc")
clock.place(x=120, y=270)

lbl1 = tk.Label(win, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=120, y=400)

lbl2 = tk.Label(win, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=280, y=400)

lbl3 = tk.Label(win, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=450, y=400)

lbl4 = tk.Label(win, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef").place(x=670, y=400)


temp_lable = tk.Label(win, font=("arial", 70, "bold"), fg="#e355cd")
temp_lable.place(x=590, y=170)
condition_lable = tk.Label(win, font=("arial", 15, "bold"), fg="#4b4bcc")
condition_lable.place(x=590, y=270)
wind_lable = tk.Label(win, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
wind_lable.place(x=120, y=430)
humidity_lable = tk.Label(win, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
humidity_lable.place(x=280, y=430)
description_lable = tk.Label(win, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
description_lable.place(x=450, y=430)
pressure_lable = tk.Label(win, text="...", font=("arial", 20, "bold"), bg="#1ab5ef", fg="#404040")
pressure_lable.place(x=670, y=430)


win.mainloop()