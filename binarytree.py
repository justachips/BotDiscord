class Node :
  def __init__(self,data):
    self.data = data
    self.right_child = None
    self.left_child = None

  def add_node(self,new_data,old_data, yes_no):
    if old_data == self.data:
      new_node = Node(new_data)
      print(yes_no)
      if yes_no == "Oui":
        self.right_child = new_node
      if yes_no == "Non":
        self.left_child = new_node
    else:
      if self.right_child != None: #verifie si existant
        self.right_child.add_node(new_data,old_data, yes_no) 
      if self.left_child != None:
        self.left_child.add_node(new_data,old_data, yes_no)



class Binary_tree:
  def __init__(self):
    self.first_node = None

    self.current_node = self.first_node

  def add_dataTree(self, new_data,old_data, yes_no):
    if self.first_node == None:
      self.first_node = Node(new_data)
    else:
      self.first_node.add_node(new_data,old_data, yes_no)

  def get_questionTree(self):
    if self.current_node == None:
      self.current_node = self.first_node
    return self.current_node.data

  def send_answerTree(self, answer):

    if answer == "Oui":
      self.current_node = self.current_node.right_child

    elif answer == "Non" :
      self.current_node = self.current_node.left_child

    if self.current_node == None:
      self.current_node = self.first_node #reprend a zero
      return "C'est fini"

    return self.current_node.data




# B = Binary_tree()
# B.add_dataTree("Pizza?","","")
# B.add_dataTree("Fromagio?","Pizza?","Oui")
# B.add_dataTree("Pasta?","Pizza?","Non")
# B.add_dataTree("Bolo?","Pasta?","Oui")


# print(B.get_questionTree())
# B.send_answerTree("Non")
# print(B.get_questionTree())
# B.send_answerTree("Oui")
# print(B.get_questionTree())
# B.send_answerTree("Oui")
# print(B.get_questionTree())
# B.send_answerTree("Non")
# print(B.get_questionTree())