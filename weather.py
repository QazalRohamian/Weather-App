import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


win = tk.Tk()
win.title("weather app")
win.geometry("900x500+300+200")
win.resizable(False, False)



win.mainloop()