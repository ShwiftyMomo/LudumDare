from Item import Item
from Player import Player
from Enemy import Enemy
from Board import Board


B=Board()

P=Player()
P.intro()


Running=True
while Running:
    B.turn(P)
