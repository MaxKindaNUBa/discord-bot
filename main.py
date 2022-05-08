import disnake as discord
from disnake.ext import commands
from generalCogs import userCmds
from modCogs import modCmds

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print("Bot it logged in as : {0.user}".format(bot))


@bot.command()
async def hello(ctx):
    await ctx.send("Hi")

bot.add_cog(userCmds.UserCmds(bot))
bot.add_cog(modCmds.Moderation(bot))
bot.run("Get your own tag")

