import discord

intents = discord.Intents.all()

from discord.ext import commands

client = commands.Bot(command_prefix="!", intents = intents)

@client.command(name="Hello")
async def delete(ctx):
    messages = await ctx.channel.history(limit=10)

    for each_message in messages:
        await each_message.delete()

@client.event
async def on_ready():
    print("Le bot est prêt !")

@client.event
async def on_typing(channel, user, when):
     await channel.send(user.name+" is typing")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044900412551073832)
    await general_channel.send("Bienvenue sur le serveur ! "+ member.name)
    await member.send("yo c automatic")

@client.event

async def sending_mp(member):
    await everyone.send("salut")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message.content = message.content.lower()

  if message.content.startswith("test"):
    await message.channel.send("tg")
    await message.channel.send("tamere")


  if "cochon" in message.content:
    await message.channel.send(R)

  if message.content == "azerty":
    await message.channel.send("qwerty")

    await client.process_commands(message)


client.run("MTE2NzM5ODMwODA1NTA4OTIwMg.GYt-O6.KAvKXWICYrKUzmg-Co9X8wKfGUFveNsONX2ZLw")