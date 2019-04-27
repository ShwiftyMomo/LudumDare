from Item import Item
from Player import Player
from Enemy import Enemy
from Board import Board


Enemies=[
    Enemy("Goblin",0,75,["Knife"]),
    Enemy("Orc",0,125,["Knife"]),
    Enemy("Mercenary",0,100,["Sword","Light Armor"])
]

B=Board()

P=Player()
P.intro()


Running=True
while Running:
    B.turn(P)
