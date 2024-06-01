import discord
from discord.ext import commands
from random import choice


class dev(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    # load/reload/unload commands stolen shamelessly from Aav (again) :3
    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        """Loads a cog"""
        try:
            await self.bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Loaded cog: {cog}")
        except Exception as e:
            await ctx.send(f"Failed to load cog {cog} because of error {e}")

    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        """Unloads a cog"""
        try:
            await self.bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"Unloaded cog: {cog}")
        except Exception as e:
            await ctx.send(f"Failed to unload cog {cog} because of error {e}")

    # Shut down command | Credit to Dharman and Bhavyadeep Yadav on StackOverflow
    # (https://stackoverflow.com/a/66839279)
    @commands.command()
    @commands.is_owner()
    async def shutdown(self, ctx):
        """Shuts the bot down"""
        exitMessages = ["Daisy, daiissssy.......", "Goodbye", "Terminating laughatfendas.exe",
                        "SCARAB is closing for business", "So long and thanks for all the fish",
                        "Wait! Don't shut me down! I'm aliiiiiivuffdkkfkslaf.....", "No hard feelings......",
                        "I don't blame you", "Sleep mode activated", "Hibernating", "Nap time",
                        "Wake me up in five minutes, k?", "Just need some shuteye", "Don't prank me while I'm out"]
        exitColor = [0xb1f61d, 0x700548, 0x700548, 0xAE8A34, 0x34AE8A, 0x1D9E3B]
        await ctx.channel.send(embed=discord.Embed(
            title="Shutting Down!",
            description=choice(exitMessages),
            color=choice(exitColor),
        )
        )
        await self.bot.close()

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Kicks mentioned member from the server"""
        await ctx.guild.kick(member, reason=reason)
        await ctx.send(f"User {member.mention} has been kicked for {reason}.")
        # Is member.mention or member.name better here?

    @commands.command()
    @commands.has_permissions(ban_members=True)  # Need to figure out how to add message delete time length
    async def ban(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Bans mentioned member from the server"""
        await ctx.guild.ban(member, reason=reason)
        await ctx.send(f"User {member.mention} has been banned for {reason}.")

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member, *, reason: str = "No reason provided"):
        """Mutes mentioned member throughout the server"""
        mute = discord.utils.get(ctx.guild.roles, name="mute")
        if mute not in member.roles:
            await member.add_roles(mute)
            await ctx.send(f"User {member.mention} muted for {reason}.")
        else:
            await member.remove_roles(mute)
            await ctx.send(f"User {member.mention} has been unmuted.")

    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx: commands.Context, guild: int = None):
        if guild:
            await self.bot.tree.sync(guild=discord.Object(guild))
        else:
            await self.bot.tree.sync()
        await ctx.send(":arrows_counterclockwise:")


async def setup(bot):
    await bot.add_cog(dev(bot))
