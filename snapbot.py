import os, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('SERVER_TOKEN')

bot = commands.Bot(command_prefix = '}')

def safemessage(msg: str):

    safe = 'bruh. BRUH!,?'
    return all(c in safe for c in msg)

@bot.event
async def on_ready():
    server = discord.utils.get(bot.guilds, name = SERVER)
    
    print(f"{bot.user} is connected to the following server:")
    print(f"{server.name}(id: {server.id})")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    # print(str(message.channel))
    # print(str(message.content))

    print(f"Deleting '{message.content}'!")
    await message.delete()

bot.run(TOKEN)