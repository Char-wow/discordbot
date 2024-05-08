# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 19:42:59 2024

@author: charl
"""

import discord
import os
from dotenv import load_dotenv
#

#ENV values
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
#

#Connecting to discord
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
          
          
          
def connect():
  intents = discord.Intents.default()
  intents.message_content = True
  client = MyClient(intents=intents)
  client.run(token)