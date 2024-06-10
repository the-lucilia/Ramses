# Staging

import discord
from discord import app_commands
from discord.ext import commands


class load_up(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def here(self, interaction: discord.Interaction):
        user = interaction.user
        role = discord.utils.get(user.guild.roles, name="Test Role")
        user_roles = user.roles
        if role not in user_roles:
            await user.add_roles(role, reason="Here Command", atomic=True)
            await interaction.response.send_message(f"Welcome to the Raid, {user.display_name}!")
        else:
            await interaction.response.send_message(f"You're already masked, {user.display_name}!")

    @app_commands.command()
    async def bye(self, interaction: discord.Interaction):
        user = interaction.user
        role = discord.utils.get(user.guild.roles, name="Test Role")
        user_roles = user.roles
        if role in user_roles:
            await user.remove_roles(role, reason="Here Command", atomic=True)
            await interaction.response.send_message(f"Sad to see you go, {user.display_name}!")
        else:
            await interaction.response.send_message(f"I can't remove what you don't have, {user.display_name}!")


async def setup(bot):
    await bot.add_cog(load_up(bot))