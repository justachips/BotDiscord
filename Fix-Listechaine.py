#on recree une liste chainer = enssemble de data,

#Crée ma node

class node:
  def __init__(self , data):
    self.data = data
    self.next_node = None

#Crée la liste

class chained_list :
  def __init__(self):
    self.first_node = None
    self.length = 0 




#fct append


  def append(self, data):

    self.length += 1
    current_node = self.first_node
    if current_node == None:
      self.first_node = node(data)
      return

    while current_node.next_node != None:
      current_node = current_node.next_node

    current_node.next_node = node(data)



#fct get    

  def get(self,id):
    if id > self.length or id < 0:
      return
    i = 0
    current_node = self.first_node
    while i < id :
      current_node = current_node.next_node
      i += 1
    return current_node.data


#fct search return true si trouve la value

  def search(self,value):
    current_node = self.first_node

    while current_node != None:
      if current_node.data == value:
        return True
      current_node = current_node.next_node

    return False


#fct insert
  

  def insert(self,data,id): 
    if self.length < id or id < 0:
      return

    if id == 0:
      New_node = node(data)
      New_node.next_node = self.first_node
      self.first_node = New_node
      self.length += 1
      return

    i = 1
    current_node = self.first_node
    while i < id:
      current_node = current_node.next_node
      i += 1

    New_node = node(data)
    New_node.next_node = current_node.next_node
    current_node.next_node = New_node
    self.length += 1

#DELETE
    
  def delete(self, id ):
    if id > self.length-1 or id < 0:
      return
    i = 0
    current_node = self.first_node

    if id == 0:
      self.first_node = current_node.next_node
      self.length -= 1
      return
    
    while i < id :
      if i+1 == id & id == self.length-1:
        current_node.next_node = None
        self.length -= 1
        return
      elif i+1 == id:
        current_node.next_node = current_node.next_node.next_node
        self.length -= 1
        return

      current_node = current_node.next_node
      i += 1
    #mon cas
    
   








L = chained_list()

L.append(5)
L.append(6)




for i in range(L.length):
  print(L.get(i))

print("---------")

L.delete(1)

print("---------")



for i in range(L.length):
  print(L.get(i))





#L.append(5)
#L.append(7)
#L.append(8)


#print(L.length)
#print(L.get(2))

#L.insert(1,3)
#print(L.get(3))
