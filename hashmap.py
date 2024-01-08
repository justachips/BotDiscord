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
        self.length += 1
        current_node = self.first_node
        if current_node is None:
            self.first_node = Node(data)
            return

        while current_node.next_node is not None:
            current_node = current_node.next_node

        current_node.next_node = Node(data)

    def getChainedList(self, id):
        if id > self.length or id < 0:
            return
        i = 0
        current_node = self.first_node
        while i < id:
            current_node = current_node.next_node
            i += 1
        return current_node.data

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

    def deleteChainedList(self, id):
        if id > self.length - 1 or id < 0:
            return
        i = 0
        current_node = self.first_node

        if id == 0:
            self.first_node = current_node.next_node
            self.length -= 1
            return

        while i < id:
            if i + 1 == id & id == self.length - 1:
                current_node.next_node = None
                self.length -= 1
                return
            elif i + 1 == id:
                current_node.next_node = current_node.next_node.next_node
                self.length -= 1
                return

            current_node = current_node.next_node
            i += 1


def showHashMap(user_history_map, user_key):
    user_history = user_history_map.get_history(user_key)
    if user_history:
        print(f"User {user_key} History:")
        current_node = user_history.first_node
        while current_node is not None:
            key, value = current_node.data
            print(f"Key: {key}, Value:")
            inner_current_node = value.first_node
            while inner_current_node is not None:
                print(inner_current_node.data)
                inner_current_node = inner_current_node.next_node
            current_node = current_node.next_node
    else:
        print(f"No history found for user {user_key}")


# # Example usage:

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

# # Set user histories in the hashmap
# map.setKeyValueHashMap("user1", user1_history)
# map.setKeyValueHashMap("user2", user2_history)

# # Show user histories
# showHashMap(map, "user1")
# showHashMap(map, "user2")
# showHashMap(map, "user3")  # Non-existent user