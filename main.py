import discord
import os
from replit import db
import neuralintents
from keep_alive import keep_alive
import random
import sys
import datetime
import roast_list
import json
import requests
import math

client = discord.Client()
intents = discord.Intents.all()

assistant = GenericAssistant('intents.json')
assistant.train_model()
assistant.save_model()

mappings = {
    "hello": hello,
    "age": age,
    "name": name,
    "time": time,
    "date": date,
    "favsong": favsong,
    "favcolor": favcolor,
    "favanimal": favanimal,
    "favfood": favfood,
    "weather_report": weather_report,
    "feels_like": feels_like,
    "min_max": min_max,
    "sunrise": sunrise,
    "sunset": sunset,
    "temp": temp
}


# Short answer questions

async def age(ctx):
    await ctx.send("I am 69420 years old")


async def name(ctx):
    await ctx.send("My name is Duck God jr")


async def favsong(ctx):
    await ctx.send("My favourite song is Never gonna give you up")


async def favfood(ctx):
    await ctx.send("Pizza, Pizza is my favourite food")


async def favanimal(ctx):
    await ctx.send("The duck is my favourite animal")


async def favcolor(ctx):
    await ctx.send("My favourite color is blue")


async def hello(ctx):
  hellores = ["Hello", "Hi there", "Wassup", "Hello there"]
  await ctx.send(random.choice(hellores))


async def date(ctx):
    await ctx.send(f"The date today is: {datetime.date.today()}")


async def time(ctx):
  now = datetime.datetime.now()
  timern = now.strftime("%I:%M %p")
  await ctx.send(f'The time right now is: {timern}')

# Weather

apikey = "6f9aa23390668e72710bd5a33e3d575c"
city = "Auckland"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
weather_response = requests.get(url).json()

async def temp(ctx):
  temp = weather_response['main']['temp']
  temp = math.floor(temp-273.15)
  await ctx.send(f"The temperature is {temp} degrees celsius")

async def feels_like(ctx):
  feelslike = weather_response['main']['feels_like']
  feelslike = math.floor(feelslike-273.15)
  await ctx.send(f"It feels like {feelslike} degrees celsius")

async def min_max(ctx):
  min = weather_response['main']['temp_min']
  min = math.floor(min-273.15)
  max = weather_response['main']['temp_max']
  max = math.floor(max-273.15)
  await ctx.send(f"Minimum Temperature today is {min} And the max will be {max}")
    
async def description(ctx):
  desc = weather_response['main'][0]["description"]
  main = weather_response['main'][0]['main']
  await ctx.send(f"Weather description {main}, {desc}")

async def sunset(ctx):
  stime = weather_response['sys']['sunset']
  sunset = datetime.datetime.fromtimestamp(stime).strftime("%I:%M %p")
  await ctx.send(f"Sunset is at {sunset}")
    
async def sunrise(ctx):
  stime = weather_response['sys']['sunrise']
  sunrise = datetime.datetime.fromtimestamp(stime).strftime("%I:%M %p")
  await ctx.send(f"Sunrise is at {sunrise}")

def weather_report():
    feels_like()
    min_max()
    sunrise()
    sunset()
    temp()


@client.event
async def on_ready():
  print("ready")

@client.event
async def on_message(ctx):
  if ctx.content.startswith("$"):
    response = assistant.request(ctx)
    await ctx.send(response)
    

keep_alive()
client.run(os.environ['Token']) 