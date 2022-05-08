import disnake as discord
from disnake.ext import commands

class UserCmds(commands.Cog):
    @commands.command(aliases=['who', 'info'])
    @commands.has_permissions(kick_members=True)
    async def whois(self,ctx, member: discord.Member):
        embed = discord.Embed(title=member.display_name+'#'+member.discriminator + '  <:ballot_box_with_check:941349699485589576>',
                              description=f"Click to view avatar: [Avatar]({member.avatar.url})",
                              colour=discord.Colour.red())
        embed.add_field(name='User ID',
                        value=str(member.id)+"\n\u200b",
                        inline=True)
        embed.add_field(name="Roles: ",
                        value=",".join([i.mention for i in member.roles]),
                        inline=True)

        embed.add_field(name='Join Date and Time',
                        value=member.joined_at.strftime("%B %d , %Y (%A)\nAt Time : %H-%M-%S %p ")+"\n\u200b",
                        inline=False)
        embed.add_field(name="Account Created on: ",
                        value=member.created_at.strftime("%B %d , %Y (%A)\nAt Time : %H-%M-%S %p "),
                        inline=True)

        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(icon_url=ctx.author.avatar.url,
                         text='Requested by: ' + ctx.author.name + '#' + ctx.author.discriminator)
        await ctx.send(embed=embed)

    @commands.command(aliases=['sinfo','si'])
    async def serverinfo(self,ctx):
        totcount = ctx.guild.member_count
        botcount = len([member for member in ctx.guild.members if member.bot])
        humancount = totcount - botcount
        embed = discord.Embed(title="Information about : "+ctx.guild.name,
                              description=f"Click to view avatar: [Avatar]({ctx.guild.icon.url})",
                              colour=discord.Colour.green())
        embed.add_field(name="Server ID :",value=str(ctx.guild.id))
        embed.add_field(name="Roles :",value=f"**{len(ctx.guild.roles)}** roles")
        embed.add_field(name="Owner name: ",value=str(ctx.guild.owner)+"\n\u200b")
        embed.add_field(name="Membercount: ",value=f"**{totcount}** in total\n**{humancount}** : humans\n**{botcount}** : bots")
        embed.add_field(name="Channels :",value=f"**{len(ctx.guild.text_channels)}** : Text channels\n**{len(ctx.guild.voice_channels)}** : Voice channels")
        await ctx.send(embed=embed)