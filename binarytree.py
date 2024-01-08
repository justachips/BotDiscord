from tools import *

class Node :
  def __init__(self,data):
    self.data = data
    self.right_child = None
    self.left_child = None

  def add_node(self,new_data,old_data, yes_no):
    if old_data == self.data:
      new_node = Node(new_data)
      # print(yes_no)
      if yes_no == "1":
        self.right_child = new_node
      if yes_no == "2":
        self.left_child = new_node
    else:
      if self.right_child != None: #verifie si existant
        self.right_child.add_node(new_data,old_data, yes_no) 
      if self.left_child != None:
        self.left_child.add_node(new_data,old_data, yes_no)



class BinaryTree:
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

    if answer == "1":
      self.current_node = self.current_node.right_child

    elif answer == "2" :
      self.current_node = self.current_node.left_child
      
    elif answer == "reset":
      self.current_node = self.first_node #reprend a zero
      return "C'est fini"

    if self.current_node == None:
      self.current_node = self.first_node #reprend a zero
      return "C'est fini"

    return self.current_node.data




MyTree = BinaryTree()
MyTree.add_dataTree("Préfère tu les jeux multijoueurs(1) ou les jeux solo(2)","","")

MyTree.add_dataTree("Prèfère tu les jeux tryhard(1) ou chill?(2)","Préfère tu les jeux multijoueurs(1) ou les jeux solo(2)","1")
MyTree.add_dataTree("Prèfère tu les jeux d'aventure(1) ou les jeux de sport?(2)","Préfère tu les jeux multijoueurs(1) ou les jeux solo(2)","2")


MyTree.add_dataTree("Préfère tu les jeux de Tir(1) ou les jeux de sport?(2)","Prèfère tu les jeux tryhard(1) ou chill?(2)","1")
MyTree.add_dataTree("Apporte tu une importance au graphique(1) ou peut importe(2)?","Prèfère tu les jeux tryhard(1) ou chill?(2)","2")

MyTree.add_dataTree("Prèfère tu les univers fictif(1) ou réel(2)?","Prèfère tu les jeux d'aventure(1) ou les jeux de sport?(2)","1")
MyTree.add_dataTree("Prèfère tu les jeux de balles(1) ou les jeux de voitures(2)?","Prèfère tu les jeux d'aventure(1) ou les jeux de sport?(2)","2")


MyTree.add_dataTree("Joue à Valorant !","Préfère tu les jeux de Tir(1) ou les jeux de sport?(2)","1")
MyTree.add_dataTree("Joue à Rocket league!","Préfère tu les jeux de Tir(1) ou les jeux de sport?(2)","2")

MyTree.add_dataTree("Joue a Rust!","Apporte tu une importance au graphique(1) ou peut importe(2)?","1")
MyTree.add_dataTree("Joue a Minecraft!","Apporte tu une importance au graphique(1) ou peut importe(2)?","2")

MyTree.add_dataTree("Joue a Cyberpunk!","Prèfère tu les univers fictif(1) ou réel(2)","1")
MyTree.add_dataTree("Joue a Red dead Redemption 2!","Prèfère tu les univers fictif(1) ou réel(2)?","2")

MyTree.add_dataTree("Joue a Fifa!","Prèfère tu les jeux de balles(1) ou les jeux de voitures(2)?","1")
MyTree.add_dataTree("Joue a Need for speed!","Prèfère tu les jeux de balles(1) ou les jeux de voitures(2)?","2")

# print(B.get_questionTree())
# B.send_answerTree("Non")
# print(B.get_questionTree())
# B.send_answerTree("Oui")
# print(B.get_questionTree())
# B.send_answerTree("Oui")
# print(B.get_questionTree())
# B.send_answerTree("Non")
# print(B.get_questionTree())