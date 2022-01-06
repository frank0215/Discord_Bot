import discord
from discord.ext import commands
import json
import os

'''
setting.json stores some important information
such as bot's token which allows us to connect to the discord server and launch the bot normally.
'''
with open('setting.json', 'r') as f:
    data = json.load(f)

'''
Prefix should be added, otherwise, you may accidentally trigger the event and launch the bot.
'''
bot = commands.Bot(command_prefix='%%')

@bot.event
async def on_ready():
    print('Bot is online')

'''
We can still write a new function for the bot while it is running.
We don't need to shut down the bot first.
'''
@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'cmds.{extension.lower()}')
    await ctx.send(f'{extension} has loaded')

'''
We can cancel some unneccessary functions. 
We don't need to shut down the bot first.
'''
@bot.command()
async def unload(ctx, extension):
    bot.unload_extension(f'cmds.{extension.lower()}')
    await ctx.send(f'{extension} has unloaded')


'''
We can still reload some existing functions for the bot while it is running.
We don't need to shut down the bot first.
'''
@bot.command()
async def reload(ctx, extension):
    bot.reload_extension(f'cmds.{extension.lower()}')
    await ctx.send(f'{extension} has reloaded')

'''
Another way to import other python file from other directory folder.
Thus, we don't need to write a lots of "import" syntax in the beginning of lines.
'''
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

'''
Run bot in while loop to make sure it always connect to the server.
'''
if __name__ == '__main__':
    while True:
        bot.run(data['TOKEN'])