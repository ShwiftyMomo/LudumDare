from Item import Item
from Player import Player
from Enemy import Enemy
from Board import Board
from King import King

print(" _____                _ _ ")
print("/  ___|              | | |")
print("\ `--.  ___ _ __ ___ | | |")
print(" `--. \/ __| '__/ _ \| | |")
print("/\__/ / (__| | | (_) | | |")
print("\____/ \___|_|  \___/|_|_|")
print("\n \n")
                          
                          

B=Board()

P=Player()
P.intro()



while True:
    B.turn(P)
