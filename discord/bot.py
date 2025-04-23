import os
import math
import discord
import random
import logging
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError('DISCORD_TOKEN is not set')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

logging.basicConfig(level=logging.INFO)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

# Emoji variables
HEADS = '<:heads:1285871035228360725>'
TAILS = '<:tails:1285871128027467848>'
DICE = '<:dice:1285874193392734228>'

@bot.command(name='flip', help='Flips a coin a specified number of times with a specified probability percentage of heads. The default probability is 50. The maximum number of flips is 20.')
@cooldown(1, 5, BucketType.user)
async def flip(ctx, count: int = 1, heads_probability: float = 50):
    if not (1 <= count <= 20):
        await ctx.send('The number of flips must be between 1 and 20.')
        return
    if not (0 < heads_probability < 100):
        await ctx.send('The probability must be between 0 and 100.')
        return

    heads_probability /= 100
    results = [HEADS if random.random() < heads_probability else TAILS for _ in range(count)]
    heads_count = results.count(HEADS)
    tails_count = results.count(TAILS)

    # Calculate the probability of this specific outcome
    probability = binomial(count, heads_count) * (heads_probability ** heads_count) * ((1 - heads_probability) ** tails_count)
    probability_percentage = probability * 100

    # Determine rarity rating
    rarity = (
        'Dominating!!' if probability_percentage > 90 else
        'Favored!' if probability_percentage > 60 else
        'Neutral' if probability_percentage > 40 else
        'Struggling!' if probability_percentage > 10 else
        'Hopeless!!'
    )

    await ctx.send(
        ''.join(results) +
        f'\nHeads: {heads_count} {HEADS} \nTails: {tails_count} {TAILS}' +
        f'\nProbability of Heads: {heads_probability*100:.2f}%' +
        f'\nProbability of this sequence: {probability_percentage}%' +
        f'\nRarity: {rarity}'
    )

@bot.command(name='roll', help='Rolls a die a specified number of times with a specified number of sides. The default number of rolls is 1 and the default number of sides is 6. The maximum number of rolls is 20 and the maximum number of sides is 120.')
@cooldown(1, 5, BucketType.user)
async def roll(ctx, count: int = 1, sides: int = 6):
    if not (1 <= count <= 20):
        await ctx.send('The number of rolls must be between 1 and 20.')
        return
    if not (2 <= sides <= 120):
        await ctx.send('The number of sides must be between 2 and 120.')
        return

    results = [random.randint(1, sides) for _ in range(count)]
    
    # Calculate the probability of this specific outcome
    probability = (1 / sides) ** count
    probability_percent = probability * 100
    
    # Determine rarity rating
    rarity = (
        'Dominating!!' if probability_percent > 90 else
        'Favored!' if probability_percent > 60 else
        'Neutral' if probability_percent > 40 else
        'Struggling!' if probability_percent > 10 else
        'Hopeless!!'
    )

    await ctx.send(DICE + ' ' + ' '.join(map(str, results)) +
                f'\nProbability of this sequence: {probability_percent}%' +
                f'\nRarity: {rarity}'
    )

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f'This command is on cooldown. Please try again in {error.retry_after:.2f} seconds')
    elif isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('You are missing a required argument')
    elif isinstance(error, commands.errors.BadArgument):
        await ctx.send('One of your arguments is not valid')
    else:
        await ctx.send('An error occurred')
        logging.error(error)

bot.run(TOKEN)
