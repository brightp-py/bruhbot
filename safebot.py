import os, discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('SERVER_TOKEN')

bot = commands.Bot(command_prefix = '}')

modchannels = ["mods", "announcements"]
EXPLAIN = "This Discord is a public record of conversations that the staff have access to.  To prevent people from accidentally talking about the questions early and potentially breaking the honor code, we have limited this server to only 'bruh' and similar messages.  Thanks for understanding!"

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

    if str(message.channel) in modchannels:
        pass

    elif str(message.channel) == "bruh":

        if message.content == "explain":
            await message.channel.send(EXPLAIN)
            await message.delete()

        # elif small == words[wcount] and wcount >= 0:
        #     pass

        # elif small == words[wcount + 1]:
        #     print(f"wcount: {str(wcount)}")
        #     wcount += 1
        #     if wcount == len(words):
        #         message.channel.send("Song completed!  gg!")

        elif not safemessage(message.content) or len(message.attachments) > 0:
            wcount = -1
            print(f"Deleting '{message.content}' ({message.author})")
            await message.delete()
        
    else:
        print(f"Deleting '{message.content}' ({message.author}) in #{message.channel}")
        await message.delete()

bot.run(TOKEN)