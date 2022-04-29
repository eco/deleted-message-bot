import discord
from datetime import datetime
import os
from dateutil.tz import *

intents = discord.Intents().default()

client = discord.Client(intents=intents)

embedData = {
    "deleted": {"colour": 0xCC0000, "title": "Message Deleted"},
    "edited": {"colour": 0xFFCC00, "title": "Message Edited"},
}


async def buildEmbed(messages, triggertype):
    embedMessage = discord.Embed(
        title=f"{embedData[triggertype]['title']}",
        description="",
        color=embedData[triggertype]["colour"],
    )
    embedMessage.set_author(name=messages[0].author.name)
    embedMessage.set_thumbnail(url=messages[0].author.avatar_url)
    embedMessage.add_field(
        name="Channel", value=messages[0].channel.mention, inline=True
    )
    embedMessage.add_field(name="Message ID", value=messages[0].id, inline=True)
    if triggertype == "edited":
        embedMessage.add_field(
            name="Before:", value=f"`{messages[0].content}`", inline=False
        )
        embedMessage.add_field(
            name="After:", value=f"`{messages[1].content}`", inline=False
        )
    else:
        embedMessage.add_field(
            name="Content:", value=f"`{messages[0].content}`", inline=False
        )
    embedMessage.set_footer(
        text=f"User ID: {messages[0].author.id} | {datetime.now().strftime('%m/%d/%Y %H:%M:%S')} {datetime.now(tzlocal()).tzname()}"
    )
    return embedMessage


@client.event
async def on_ready():
    print("Logged in.")


@client.event
async def on_message_delete(message):
    print()
    removeEmbed = await buildEmbed([message], "deleted")
    await message.guild.get_channel(int(os.environ.get("LOG_CHANNEL"))).send(
        embed=removeEmbed
    )


@client.event
async def on_message_edit(before, after):
    if before.author.id != int(os.environ.get("BOT_ID")):
        editEmbed = await buildEmbed([before, after], "edited")
        await before.guild.get_channel(int(os.environ.get("LOG_CHANNEL"))).send(
            embed=editEmbed
        )


client.run(os.environ.get("TOKEN"))
