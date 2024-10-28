# WARN : This script has not been tested both on Linux and Bot wise.

import discord
import json
from discord.ext import commands
from _lib_sniff import enable_monitor_mode, sniff_packets


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')


@bot.command()
async def send_pcap(ctx, filepath='capture.pcap'):
    await ctx.send(file=discord.File(filepath))


@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user:
        return

    if reaction.emoji == '🔍':  # Start sniffing
        enable_monitor_mode()
        sniff_packets()
        await reaction.message.channel.send('Sniffing started.')
    elif reaction.emoji == '🔓':  # Start cracking (placeholder)
        await reaction.message.channel.send('Cracking started.')
    elif reaction.emoji == '🔎':  # Start scanning (placeholder)
        await reaction.message.channel.send('Scanning started.')


with open('config.json') as config_file:
    config = json.load(config_file)
bot.run(config['DISCORD_BOT_TOKEN'])
