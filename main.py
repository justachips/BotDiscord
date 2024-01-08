import discord
from discord.ext import commands
from hashmap import *
from tools import *

user_history_map = HashMap(50)
intents = discord.Intents.all()

client = commands.Bot(command_prefix="!", intents=intents)

# @client.command(name="Hello")
# async def delete(ctx):
#     messages = await ctx.channel.history(limit=10)

#     for each_message in messages:
#         await each_message.delete()
        
@client.command(name="h-show") #show all
async def showAllHistory(ctx, user_key):
    await showHashMap(ctx, user_history_map, user_key)
    
@client.command(name="h-last") #last command
async def showLastHistory(ctx, user_key):
    await showLastHashMap(ctx, user_history_map, user_key)
    
@client.command(name="h-del") #delete
async def delete_history(ctx, user_key):
    result_message = deleteChainedList(user_history_map, user_key)
    await ctx.send(result_message)
    
@client.command(name="h-nav") #navigate
async def delete_history(ctx, user_key):
    result_message = deleteChainedList(user_history_map, user_key)
    await ctx.send(result_message)




# @client.event
# async def on_typing(channel, user, when):
#     await channel.send(user.name + " is typing")

@client.event
async def on_member_join(member):
    general_channel = client.get_channel(1044900412551073832)
    await general_channel.send(cadre("Bienvenue sur le serveur ! " + member.name))
    await member.send("yo c automatic")

# @client.event
# async def sending_mp(member):
#     await everyone.send("salut")
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    message.content = message.content.lower()

    # creat a new history or append a existing one
    
    user_key = str(message.author.name)  # the keys is the name of the user
    user_history = user_history_map.get_history(user_key)
    print(user_key)
    if not user_history:
        user_history = ChainedList()
        user_history_map.setKeyValueHashMap(user_key, user_history)
        print("user créé!")

    # Append 
    user_history.appendChainedList(message.content)
    
    if message.content.startswith("test"):
        await message.channel.send(cadre("tg"))

    await client.process_commands(message)






#run the bot with a token


token = myToken()
print()
print("Botchips run with the token:", token)
print()
client.run(token)
