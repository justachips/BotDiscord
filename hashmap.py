import discord
from discord.ext import commands
from datetime import datetime
from tools import *

intents = discord.Intents.all()
client = commands.Bot(command_prefix="!", intents=intents)



class HashMap:
    def __init__(self, size):
        self.buckets = {}
        for i in range(size):
            self.buckets[i] = ChainedList()

    def setKeyValueHashMap(self, key, data):
        index = hash(key) % len(self.buckets)
        linked_list = self.buckets[index]

        # Append the key and linked list to the hashmap
        linked_list.appendChainedList((key, data))

    def get_history(self, key):
        index = hash(key) % len(self.buckets)
        linked_list = self.buckets[index]

        return linked_list


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class ChainedList:
    def __init__(self):
        self.first_node = None
        self.length = 0

    def appendChainedList(self, data):
        timestamp = datetime.now()
        timestamp_str = timestamp.strftime("%m/%d %H:%M   :   ")

        self.length += 1
        current_node = self.first_node

        if current_node is None:
            self.first_node = Node((timestamp_str + data))
            return

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = Node((timestamp_str + data))

    def getChainedList(self, id):
        if id > self.length or id < 0:
            return
        i = 0
        current_node = self.first_node
        while i < id:
            current_node = current_node.next_node
            i += 1
        return current_node.data
    
    def deleteAllChainedList(self):
        self.first_node = None
        self.length = 0

    def searchChainedList(self, value):
        current_node = self.first_node
        while current_node is not None:
            if current_node.data == value:
                return True
            current_node = current_node.next_node
        return False

    def insertChainedList(self, data, id):
        if self.length < id or id < 0:
            return

        if id == 0:
            new_node = Node(data)
            new_node.next_node = self.first_node
            self.first_node = new_node
            self.length += 1
            return

        i = 1
        current_node = self.first_node
        while i < id:
            current_node = current_node.next_node
            i += 1

        new_node = Node(data)
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        self.length += 1

def deleteChainedList(user_history_map, user_key):
    user_history = user_history_map.get_history(user_key)
    if user_history:
        user_history.deleteAllChainedList() 
        return cadre(f"Success! History deleted for {user_key}.")
    else:
        return cadre(f"Error! no history found for {user_key}.")


# adapter pour discord
#get all msg from history
async def showHashMap(ctx, user_history_map, user_key):
    user_history = user_history_map.get_history(user_key)
    if user_history:
        result_message = f"User {user_key} History:\n"
        current_node = user_history.first_node
        while current_node is not None:
            message_data = current_node.data
            result_message += f"{message_data}\n"
            current_node = current_node.next_node
        await ctx.send(cadre(result_message))
    else:
        await ctx.send(cadre(f"Error! no history found for {user_key}"))
        
        
#get last message from history
async def showLastHashMap(ctx, user_history_map, user_key):
    user_history = user_history_map.get_history(user_key)
    if user_history:
        result_message = f"User {user_key} History:\n"
        current_node = user_history.first_node
        while current_node.next_node is not None:
            message_data = current_node.data
            result_message = f"{message_data}\n"
            current_node = current_node.next_node
        await ctx.send(cadre(result_message))
    else:
        await ctx.send(cadre(f"Error! no history found for  {user_key}"))
        
        
        


#navigate



# Example usage:

# # Create a hashmap
# map = HashMap(10)

# # Create user history linked lists
# user1_history = ChainedList()
# user2_history = ChainedList()

# # Append data to user history linked lists
# user1_history.appendChainedList("Event 1")
# user1_history.appendChainedList("Event 2")

# user2_history.appendChainedList("Event A")
# user2_history.appendChainedList("Event B")



# user1_history.getChainedList(user1_history.length-1)

# # Set user histories in the hashmap
# map.setKeyValueHashMap("user1", user1_history)
# map.setKeyValueHashMap("user2", user2_history)

# # Show user histories
# showHashMap(map, "user1")
# showHashMap(map, "user2")
# showHashMap(map, "user3")  # Non-existent user

