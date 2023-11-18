import discord
import os
import random
from discord.ext import commands
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def pollution_suggest(ctx):
    await ctx.send(f"Stay Informed Stay updated on air quality levels in your area. Many countries and cities have websites or mobile apps that provide real-time air quality information. Use these resources to plan your outdoor activities. Limit Outdoor Activities on Poor Air Quality Days These devices can help remove indoor air pollutants, making your indoor air cleaner and safer to breathe.")

@bot.command()
async def pwd(ctx, pass_length = 8):
    await ctx.send(gen_pass(pass_length))

@bot.event
async def on_member_join(member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(to_send)

@bot.command()
async def guess(ctx):
    global guess_game

    guess_game = random.randint(1,10)
    await ctx.send("Guess a number between 1 and 10.")

@bot.command()
async def answer(ctx, number):
    if guess_game == int(number):
        await ctx.send("Correct!")
    else:
        await ctx.send("That's wrong, try again.")

@bot.command()
async def meme(ctx):
    with open('images/MEME1.jpg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

bot.run("MTE0MjI5NzA3NjM3NDQzNzg4OQ.G5yep6.DGGTmUKSNR9BhhMlFq8_8LuUzm3B6UWTQw4Jno")