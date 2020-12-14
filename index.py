import discord
from discord.ext import commands

TOKEN = open('token.txt', 'r').readline()
client = commands.Bot(command_prefix='ch !')

client.remove_command('help')


@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed()
    embed.title = 'Help/About'
    embed.add_field(name='The Null Command', value='It does nothing.', inline=False)

    await ctx.send(embed=embed)

client.run(TOKEN)
