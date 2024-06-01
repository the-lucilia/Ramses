"""
roll_out is the actual tag command, and it runs the actual tag raids and during update commands.
"""
import discord
from discord.ext import commands
from discord import app_commands
import aiosqlite


class roll_out(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command()
    async def roll_out(self, interaction: discord.Interaction):
        await interaction.response.send_message("Roll out!")

    @app_commands.command()
    async def tag(self, interaction: discord.Interaction,
                  number_targets: int,
                  trigger_length: int,
                  switch_length: int,
                  allow_governor: bool,
                  ):
        sql_command_file = open('SQL_Files/all_targets_no_gov.sql', 'r')
        sql_command = sql_command_file.readlines()
        sql_command = sql_command[0]
        async with aiosqlite.connect('regions.db') as db:
            async with db.execute(sql_command) as cursor:
                targets_array = []
                for row in await cursor.fetchall():
                    targets_array.append(row[1])
                print(f"Inside for loop: {targets_array}")
                await interaction.response.send_message(f'First {number_targets} targets: {targets_array[0:number_targets]}')


async def setup(bot):
    await bot.add_cog(roll_out(bot))
