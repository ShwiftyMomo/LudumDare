from Item import Item
from Job import Job
from Player import Player
from Enemy import Enemy
from Board import Board

Items=[
    Item("Sword",20,"The original, a sword.","weapon"),
    Item("Light Armor",10,"A wee bit of protection is better than none at all.","armor"),
    Item("Healing Potion",["hp",50],"Recovering health is quite important when at 1 hp.","consumable"),
    Item("Knife",10,"It's really just a small sword.","weapon")
]
Jobs=[
    Job("Warrior",25,125,["Sword","Healing Potion","Light Armor"])
]
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
