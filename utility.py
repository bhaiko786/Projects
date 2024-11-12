# This script will prompt the user to enter the directory path and then iterate through each file in that directory. For each file, it will ask the user to enter a new name, and then rename the file with the new name and same extension.
# You can save this script to a file (e.g., rename_files.py) and run it from the command line using python rename_files.py.

# import os

# def rename_files():
#     # Get the directory path from the user
#     dir_path = input("Enter the directory path: ")

#     # Get the current files in the directory
#     files = os.listdir(dir_path)

#     # Loop through each file
#     for file in files:
#         # Get the file extension
#         file_ext = os.path.splitext(file)[1]

#         # Get the new file name from the user
#         new_name = input(f"Enter new name for {file}: ")

#         # Rename the file
#         os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_name + file_ext))

#     print("Files renamed successfully!")

# rename_files()

# 👇🏻This code defines a Discord bot that listens for the !rename-file command. When a user runs this command and attaches a file and provides a new name, the bot downloads the file, renames it, and sends the renamed file back to the user.
# You'll need to replace YOUR_DISCORD_BOT_TOKEN_HERE with your actual Discord bot token.
# Note that this code assumes you have the discord.py library installed. If you don't, you can install it with pip install discord.py.
# Also, keep in mind that this is just an example and you may want to add additional error handling and features to your bot. 👇🏻

import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='rename-file')
async def rename_file(ctx, file: discord.Attachment, new_name: str):
    # Get the file and new name from the user
    file_url = file.url
    file_ext = file.filename.split('.')[-1]

    # Download the file
    async with ctx.typing():
        file_data = await file.read()
        with open(f'temp.{file_ext}', 'wb') as f:
            f.write(file_data)

    # Rename the file
    os.rename(f'temp.{file_ext}', f'{new_name}.{file_ext}')

    # Send the renamed file back to the user
    await ctx.send(file=discord.File(f'{new_name}.{file_ext}'))

bot.run('YOUR_DISCORD_BOT_TOKEN_HERE')