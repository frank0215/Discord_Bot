import discord
from discord.ext import commands
from core.classes import Cog_Extension
from crawl.beauty import Beauty
import datetime

class Entertainment(Cog_Extension):

    '''
    Give it a date(e.g. 2021-12-09 or 2021/12/09) and date range(e.g. 5)
    It would crawl the pictures from the website between 2021-12-09 ~ 2021-12-05
    the date range would be 0 by default. (i.e. one day only)
    '''
    @commands.command()
    async def beauty(self, ctx, date, period=0):
        beauty = Beauty()
        arr = beauty.getArticle(date, period)
        imgList = beauty.getImgUrl(arr)
        count_line = 0
        for img in imgList:
            count_line += 1
            await ctx.send(img)
        await ctx.send(f'{count_line} pictures')

    '''
    Give it a date and the number of pictures you want to see
    If you want to see 10 pictures in a certain date, you just need to put a parameter next to the date
    the date range is optional.
    '''
    @commands.command()
    async def nob(self, ctx, date, num:int, period=0):
        beauty = Beauty()
        arr = beauty.getArticle(date, period)
        imgList = beauty.getImgUrl(arr, num)
        count_line = 0
        for img in imgList:
            count_line += 1
            await ctx.send(img)
        await ctx.send(f'{count_line} pictures')

    '''
    Give it a date and an end date so that
    it can display the picutres within this date range.    
    '''
    @commands.command()
    async def dob(self, ctx, date, end_date):
        beauty = Beauty()
        date = datetime.datetime.strptime(date, '%Y-%m-%d')
        end_date = beauty.change_date(end_date)
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
        period = (date-end_date).days
        arr = beauty.getArticle(date, period)
        imgList = beauty.getImgUrl(arr)
        count_line = 0
        for img in imgList:
            count_line += 1
            await ctx.send(img)
        await ctx.send(f'{count_line} pictures')


def setup(bot):
    bot.add_cog(Entertainment(bot))