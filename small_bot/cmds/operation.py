import discord
from discord.ext import commands
from core.classes import Cog_Extension

'''
Inheriting from Cog_Extension which I wrote in the core folder named classses.py 
'''
class Operation(Cog_Extension):
    def __init__(self, bot):
        self.bot = bot

    '''
    Using decorator is more convenient to construct the function
    ctx means the current channel where you initiate the event
    '''
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'{round(self.bot.latency*1000, 2)} ms')

    '''
    Be careful, all parameter would be regarded as str while you putting in the parenthesis.
    So I need a write a specific type if I needed after the parameter to tell it is not a string type.
    '''
    @commands.command()
    async def purge(self, ctx, num:int):
        await ctx.channel.purge(limit=num+1)
    
def setup(bot):
    bot.add_cog(Operation(bot))