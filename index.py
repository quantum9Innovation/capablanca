import discord
from discord.ext import commands
from pythonchess import chess
from copy import deepcopy

TOKEN = open('token.txt', 'r').readline()
client = commands.Bot(command_prefix='capa ')

client.remove_command('help')
game = None


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed()
    embed.title = 'Help/About'
    embed.add_field(name='start', value='Create a game.', inline=False)
    embed.add_field(name='move', value='Only valid after a game has been created.', inline=False)
    embed.add_field(name='exit', value='Leave a game.', inline=False)

    await ctx.send(embed=embed)


@client.command()
async def start(ctx):

    global game
    game = chess.Board()

    await ctx.send('The game has started.')
    await ctx.send('Board positions are shown in algebraic notation')
    await ctx.send('Prefix algebraic notation with command `move`')
    await ctx.send('Waiting for first move ...')

    await ctx.send(game.fen())


@client.command()
async def move(ctx, note):

    global game

    if game.is_legal(game.parse_san(note)):

        game.push_san(note)

        await ctx.send(note + ' was played')
        await ctx.send(game.fen())

    else:
        await ctx.send('Illegal move!')


@client.command()
async def exit(ctx):

    global game

    game = None
    await ctx.send('Current game session has been closed.')
    await ctx.send('Use `capa start` to create a new one.')

client.run(TOKEN)
