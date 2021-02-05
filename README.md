# BruhBot
BruhBot was a tool used in the EECS 370 Fall 2020 server.  It acts an anti-cheating measure by deleting any messages except the following:
* Messages sent in administrator channels (by default, #mods and #announcements)
* Messages in #bruh that conform to a very specific set of rules (by default, a message can only contain the letters found in "bruh")

This way, the server can still be used by students to vent about an exam without the risk of breaking the honor code by discussing the exam.

## Env File
In order to use BruhBot, you need to create a .env file.  This file SHOULD NOT be uploaded to the repository or shared with anybody else.
To create the .env file, start by [creating your Discord bot](https://realpython.com/how-to-make-a-discord-bot-python/).  Your .env file should then use the following format:
```
# .env
DISCORD_TOKEN={Bot Token}
SERVER_TOKEN={Server Name}
```
The {Bot Token} can be found by going to discord.com/developers, selecting your created app, going to "Bot" on the left-hand side, and clicking "Click to Reveal Token" or "Copy".

The {Server Name} can be found by right-clicking the server, going to "Server Settings" > "Overview" > "Server Name".