import random 
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi Browh! Welcome to our server! I hope you always enjoy here! {bot.user}!')

@bot.command()
async def p(ctx):
    await ctx.send(f'Yo browh! Happy online!!! {bot.user}!')

@bot.command()
async def off(ctx):
    await ctx.send(f'Goodbye, have a nice day! {bot.user}!')

@bot.command()
async def thebotiscool(ctx):
    await ctx.send(f'Thank you for your complement!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh) 

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right) 

@bot.command()
async def multiply(ctx, left: int, right: int):
    """Times two numbers together."""
    await ctx.send(left * right) 

@bot.command()
async def minusleftisbigger(ctx, left: int, right: int):
    """Minus two numbers together."""
    await ctx.send(left - right) 

@bot.command()
async def minusrightisbigger(ctx, left: int, right: int):
    """Minus two numbers together."""
    await ctx.send(right - left) 

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices)) 

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content) 

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}, Welcome to this server!!!')






bot.run('Silahkan masukkan token mu!') 



