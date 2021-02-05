import os, discord
from dotenv import load_dotenv
from discord.ext import commands
import json

import creeper, riddle

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('SERVER_TOKEN')

with open("settings.json") as f:
    SETTINGS = json.load(f)

bot = commands.Bot(command_prefix = '}')

modchannels = SETTINGS["adminchannels"]
bruchannels = SETTINGS["bruhchannels"]
ENABLE = SETTINGS["enable"]

EXPLAIN = "This Discord is a public record of conversations that the staff have access to. To prevent people from accidentally talking about the questions early and potentially breaking the honor code, we have limited this server to only 'bruh' and similar messages.  Thanks for understanding!

bot.wcount = -1
bot.wusers = []
bot.wlives = 1

def safemessage(msg: str):

    safe = 'bruh. BRUH!,?'
    return all(c in safe for c in msg)

@bot.event
async def on_ready():
    server = discord.utils.get(bot.guilds, name = SERVER)
    
    print(f"{bot.user} is connected to the following server:")
    print(f"{server.name}(id: {server.id})")

@bot.event
async def on_message_edit(before, after):

    if ENABLE["delete-edits"] and before.content != after.content:
        print(f"Deleting '{after.content}' ({after.author})")
        await after.delete()
    
@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if ENABLE["admin-channels"] str(message.channel) in modchannels:
        pass

    elif str(message.channel) in bruchannels:

        small = creeper.makeNormal(message.content)

        if message.content == "explain":
            await message.channel.send(EXPLAIN)
            await message.delete()

        elif small == creeper.words[bot.wcount + 1]:
            if message.author not in bot.wusers:
                bot.wusers.append(message.author)
                bot.wlives += 1
            bot.wcount += 1
            print(f"wcount: {str(bot.wcount)}")
            if bot.wcount == len(creeper.words):
                await message.channel.send("Song completed!  gg!")

        elif small == creeper.words[bot.wcount] and bot.wcount >= 0:
            if message.author not in bot.wusers:
                bot.wusers.append(message.author)
                bot.wlives += 1
        
        elif x := riddle.printRiddle(message.content):
            print(x)
            await message.channel.send(x)

        elif not safemessage(message.content) or len(message.attachments) > 0:
            if x := riddle.checkSolution(message.content, str(message.author)):
                print(x)
                await message.channel.send(x)
            elif bot.wcount > -1:
                bot.wlives -= 1
                if bot.wlives < 1:
                    await message.channel.send(f"Streak of {str(bot.wcount)} broken by {message.author}...  Start over, one word per message!  The next word was '{creeper.words[bot.wcount + 1]}'")
                    bot.wcount = -1
                    bot.wlives = 1
                    bot.wusers = []
                else:
                    await message.channel.send(f"Incorrect response by {message.author}.  You have {str(bot.wlives)} left.")
            print(f"Deleting '{message.content}' ({message.author})")
            await message.delete()
    
    # elif str(message.channel) == "music-commands":

    #     if message.content[0] != "-":
    #         print(f"Deleting '{message.content}' ({message.author}) in #{message.channel}")
    #         await message.delete()
    
    else:
        print(f"Deleting '{message.content}' ({message.author}) in #{message.channel}")
        await message.delete()

bot.run(TOKEN)