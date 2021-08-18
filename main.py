import discord
from replit import db
from keep_alive import keep_alive

client = discord.Client()
intents = discord.Intents.all()

db["numrn"] = 0

@client.event
async def on_ready():
  print("ready")


keep_alive()
client.run('ODY2MTE4OTc0NTk2MDU1MDYw.YPN6Jw.PD88Epp4tWbZNzGkXPhZHgV4AWM')