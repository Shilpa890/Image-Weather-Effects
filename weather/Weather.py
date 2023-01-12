# importing the library
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def weather_data(city):
# enter city name
# create url
    url = "https://www.google.com/search?q=" + "weather" + city

    # requests instance
    html = requests.get(url).content

    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')

    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text

    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]
    t = pd.to_datetime(time, format= '%A %I:%M %p')
    htime=t.strftime('%H')
    hhtime=int(htime)
    # list having all div tags having particular class name
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})

    # particular list with required data
    strd = listdiv[5].text

    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]
    return temp,hhtime,sky,other_data
