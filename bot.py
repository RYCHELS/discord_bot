import discord
import random
import os
import requests
from discord.ext import commands
from main import genn_pass
from load_model import get_class

# Membaca token dari file token.txt
with open("Token.txt", "r") as f:
    token = f.read().strip()

# Variabel intents menyimpan hak istimewa bot
intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * count_heh)

@bot.command()
async def passw(ctx, panjang=5):
    await ctx.send(genn_pass(panjang))

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.messafe.attachments:
            file_name = attachment.file_name
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            class_name, confidence_score = get_class("converted_keras/keras_model.h5", "converted_keras/labels.txt", file_name)
            info = f"Gambar ini adalah: {class_name} \nDengan tingkat kepercayaan: {confidence_score}"
            if confidence_score < 0.5:
                info =f"maaf model tidak bisa mengenali objek"
            await ctx.send(info)
    else:
        await ctx.send("Anda lupa mengunggah gambar:(")

bot.run(token)
