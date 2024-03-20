#discord plugins
import discord
import os
from dotenv import load_dotenv

import mysql.connector
from mysql.connector import Error
import pandas as pd

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
pw = os.getenv('SQLROOTPASS')

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')
        if message.content == 'PING':
          await message.channel.send('FUCKING PONG')
          
          
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)

connection = create_server_connection("localhost", "root", pw)