import discord
from datetime import datetime
import config

intents = discord.Intents().default()

client = discord.Client(intents=intents)

#TODO Repurpose to work with other future functions. Provide title as input.
# Or dictionary with preset values for colour, title, etc based on what triggered call.
# {"deleted": {"colour": 0xCC0000, "title": "Message Deleted"}, "edited": {"colour": orange?, "title": "Message Edited"}}
async def buildEmbed(message):
    embedMessage = discord.Embed(title="Message Deleted", description="", color=0xCC0000)
    embedMessage.set_author(name=message.author.name)
    embedMessage.set_thumbnail(url=message.author.avatar_url)
    embedMessage.add_field(name="Channel", value=message.channel.mention, inline=True)
    embedMessage.add_field(name="Message ID", value=message.id, inline=True)
    embedMessage.add_field(name="Content:", value=f"`{message.content}`", inline=False)
    #Probably should set timezone to PST. Not super useful since discord message time **should** be accurate.
    embedMessage.set_footer(text=f"User ID: {message.author.id} | {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
    return embedMessage

@client.event
async def on_ready():
    print('Logged in.')

@client.event
async def on_message_delete(message):
    print(message) #Used for debugging, remove in future release.
    removeEmbed = await buildEmbed(message)
    await message.guild.get_channel(config.LOG_CHANNEL).send(embed=removeEmbed)
    
client.run(config.TOKEN)
