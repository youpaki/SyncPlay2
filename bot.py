
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
        subprocess.run(["python","maine34.py"])
        await message.channel.send('synced')


client.run("MTE2MDYyNDA2NjI0NDM5OTI0NA.GSUe7r.8G_7l99NrEWvyCWIuXkh3FOi9oXOyy8cYoiK2k")
