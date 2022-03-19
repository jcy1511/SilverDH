from ast import alias
import discord, asyncio, os
from discord.ext import commands
from sympy import false
from lolstatus import status

game = discord.Game("?help")
bot = commands.Bot(command_prefix='?', status=discord.Status.online, activity=game, help_command=None)
with open("token.txt", "r") as f :
    token = f.read()

@bot.command(aliases=['안녕', 'hi', '안녕하세요'])
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 안녕하세요!')


@bot.command(name='join')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} 님은 음성 채널에 참가하고 있지 않습니다".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("봇이 음성 채널에 참가하고 있지 않습니다")


@bot.command(aliases=['p'])
async def play(ctx, url):
    if url == "lovepoem" or url == "러브포엠" :
        filename = "songs/lovepoem.mp3"
        songname = "[앨범]Love poem - IU"
    else :
        await ctx.send(f"{url}이라는 노래 파일이 없습니다.")
        return false

    if not ctx.message.author.voice:
        await ctx.send("{} 님은 음성 채널에 참가하고 있지 않습니다".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        voice_channel.play(discord.FFmpegPCMAudio(filename))
    await ctx.send('**Now playing:** {}'.format(songname))

@bot.command(aliases=['melon'])
async def melonChartPlay(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} 님은 음성 채널에 참가하고 있지 않습니다".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

    server = ctx.message.guild
    voice_channel = server.voice_client

    async with ctx.typing():
        voice_channel.play(discord.FFmpegPCMAudio("songs/melon.mp3"))
    await ctx.send('**Now playing:** {}'.format("멜론차트 2022년 03월 16일(수) 3주차"))

@bot.command(aliases=['랭크','rank','티어','tier'])
async def lolstatus(ctx,nickname):
    await ctx.send(status(nickname))

@bot.command()
async def help(ctx):
    await ctx.send("""**명령어 목록**
    ?p [노래이름] -> 노래 재생
    ?songlist -> 보유 노래 목록
    (또는 ?sl)
    ?leave -> 음성 채널에서 내보내기

    ?rank [닉네임] -> 롤 티어 검색
    (또는 ?tier, ?랭크, ?티어)""")

@bot.command(aliases=['sl'])
async def songlist(ctx):
    await ctx.send("""**보유 노래 목록**
    [앨범]Love poem - IU""")

bot.run(token)