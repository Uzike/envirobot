import discord
from discord.ext import commands 
import requests
from my_token import my_token
from key.py import key

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='%', intents=intents)
##########################################################################
url1 = "https://climate-change-live402.p.rapidapi.com/news/nyp"

headers1 = {
	"X-RapidAPI-Key": "key",
	"X-RapidAPI-Host": "climate-change-live402.p.rapidapi.com"
}
##########################################################################

@bot.event
async def on_ready():
    print("All good.")

@bot.command('climatechange')
async def climatechange(ctx):
    responce1 = requests.get(url1, headers=headers1)
    await ctx.send(responce1.json())


bot.run("my_token")
