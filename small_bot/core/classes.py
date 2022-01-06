import discord
from discord.ext import commands

'''
Inherit from commands.Cog
Source tells the discord API document.
'''
class Cog_Extension(commands.Cog):

    '''
    Setting up the bot in this class so that 
    other classes inherited from here can have synchonized bot settings.
    '''
    def __init__(self, bot):
        self.bot = bot