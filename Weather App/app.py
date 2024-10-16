# the app that will process the weather
from flask import Flask, g, request, render_template
import requests
import json, os
from datetime import datetime


app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])


def weather():
    temprature = None
    country = ""
    skyInfo = None
    skyDescript = None
    windSpeed = None
    sunrize = None
    sunset = None
    humidity = None
    convert = ""
    shorten = ""
    #http://api.openweathermap.org/data/2.5/weather?appid=2b27032bb3515f3c1c0ef746f2b9d54d&q=london
    if request.method == "POST":
        #variable data 
        stuff = open("stuff.txt", "r").read()
        location = request.form.get('search-weather')
        url = "http://api.openweathermap.org/data/2.5/weather?"
        rUrl = url + "appid=" + stuff + "&q=" + location
        response = requests.get(rUrl).json()
        #html elements
        temprature = response["main"]["temp"]
        country = response["name"]
        skyInfo = response["weather"][0]["main"]
        skyDescript = response["weather"][0]["description"]
        windSpeed = response["wind"]["speed"]
        humidity = response["main"]["humidity"]
        convert = temprature - 273.15 # math which removed the need for the javascript lol
        shorten = round(convert, 2) # rounds so the return isnt a long decimal
        print(response)
        


    return render_template("index.html", temprature = shorten, country = country, skyinfo = skyInfo, skyDescript = skyDescript, windSpeed = windSpeed, sunrize = sunrize, sunset = sunset, humidity = humidity)

if __name__ == '__main__':
    # Start the Flask web server
    app.run(host="0.0.0.0",port=5000,debug=True)
    