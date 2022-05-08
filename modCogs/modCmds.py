import asyncio
import datetime
from disnake.ext import commands
import disnake as discord


class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.channel = None

    # Purge messages command!
    @commands.command(aliases=['cl', 'purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=0):
        if amount == 0:
            await ctx.channel.send('Give an actual number of messages to clear dumbo!')
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.channel.send('Successfully purged {0} messages!'.format(amount))

    # Kick members command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, memid: discord.Member, *, reasonn='Nothing'):
        ban_embed = discord.Embed(
            title=f"{memid.name}#{memid.discriminator} Kicked!  <:ballot_box_with_check:941349699485589576>",
            description=f"For the reason : {reasonn}",
            colour=discord.Colour.blue())
        ban_embed.set_thumbnail(url=memid.avatar.url)
        ban_embed.set_footer(icon_url=ctx.author.avatar.url,
                             text=f"Kicked By: {ctx.author.name}#{ctx.author.discriminator}")
        await memid.send(embed=ban_embed)
        await ctx.send(embed=ban_embed)
        await memid.kick(reason=reasonn)

    # Ban members command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, memid: discord.Member, *, reasonn='Nothing'):
        ban_embed = discord.Embed(
            title=f"{memid.name}#{memid.discriminator} Banned!  <:ballot_box_with_check:941349699485589576>",
            description=f"For the reason : {reasonn}",
            colour=discord.Colour.blue())
        ban_embed.set_thumbnail(url=memid.avatar.url)
        ban_embed.set_footer(icon_url=ctx.author.avatar.url,
                             text=f"Banned By: {ctx.author.name}#{ctx.author.discriminator}")
        await memid.send(embed=ban_embed)
        await ctx.send(embed=ban_embed)
        await memid.ban(reason=reasonn)

    # Unban members command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member):
        try:
            memid = await self.bot.fetch_user(member)
            await ctx.guild.unban(discord.Object(id=member))
            ban_embed = discord.Embed(
                title=f"{memid.name}#{memid.discriminator} unbanned!  <:ballot_box_with_check:941349699485589576>",
                colour=discord.Colour.blue())
            ban_embed.set_thumbnail(url=memid.avatar.url)
            ban_embed.set_footer(icon_url=ctx.author.avatar.url,
                                 text=f"Unbanned By: {ctx.author.name}#{ctx.author.discriminator}")
            await ctx.channel.send(embed=ban_embed)
        except:
            await ctx.send(ctx.author.mention + " Type in a proper user ID")

    # Temp ban command
    banned_lis = {}

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member: discord.Member, duration: int):
        await ctx.guild.ban(member)
        await asyncio.sleep(duration)
        await ctx.guild.unban(discord.Object(id=member.id))

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def timeout(self, ctx, member: discord.Member, duration, reasonn='Nothing for now'):
        time = 0
        embed = discord.Embed(title='Successfully timed out', colour=discord.Colour.teal())
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name=f"Successfully timed out {member.name}#{member.discriminator}",
                        value=f"With the reason : {reasonn}")
        embed.set_footer(icon_url=ctx.author.avatar.url,
                         text=f"Timed-out By: {ctx.author.name}#{ctx.author.discriminator}")
        if duration[-1] == "d" or duration[-1] == "D":
            time = datetime.timedelta(days=int(duration[0:-1]))
        elif duration[-1] == "w" or duration[-1] == "W":
            time = datetime.timedelta(weeks=int(duration[0:-1]))
        elif duration[-1] == "m" or duration[-1] == "M":
            time = datetime.timedelta(minutes=int(duration[0:-1]))
        elif duration[-1] == "s" or duration[-1] == "S":
            time = datetime.timedelta(seconds=int(duration[0:-1]))
        await ctx.channel.send(embed=embed)
        await member.edit(timeout=time, reason=reasonn)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def untimeout(self, ctx, member: discord.Member):
        embed = discord.Embed(title='Successfully un-timed out', colour=discord.Colour.teal())
        embed.set_thumbnail(url=member.avatar.url)
        embed.add_field(name=f"Successfully un-timed out {member.name}#{member.discriminator}",
                        value=f"Id : {member.id}")
        embed.set_footer(icon_url=ctx.author.avatar.url,
                         text=f"Timed-out By: {ctx.author.name}#{ctx.author.discriminator}")
        await ctx.channel.send(embed=embed)
        await member.edit(timeout=None)
