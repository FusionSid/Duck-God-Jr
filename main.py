import discord
import os
import neuralintents
from keep_alive import keep_alive

client = discord.Client()
intents = discord.Intents.all()

assistant = GenericAssistant('intents.json')

assistant.train_model()
assistant.save_model()

@client.command()
async def ai(ctx, *, req):
  response = assistant.request(req)
  await ctx.send(response)

keep_alive()
client.run(os.environ['Token']) 