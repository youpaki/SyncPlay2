import json
import discord
import subprocess
intents = discord.Intents.all()
client = discord.Client(command_prefix='!', intents=intents)




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('sync'):
        subprocess.run(["python","main.py"])
        await message.channel.send('synced')

with open("token.json",'r') as fp:
    token = json.load(fp)



print(token)


client.run(token)
