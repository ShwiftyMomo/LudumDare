from Item import Item
from Player import Player
from Enemy import Enemy
from Board import Board
from King import King

K=King()

B=Board()

P=Player()
P.intro()



while True:
    B.turn(P,K)
