from Enemy import Enemy
from Item import Item

class Board:
    def __init__(self):
        self.enemies=[]
        self.events=[Event("Start")]

    def turn(self,P):
        move=input()
        print("\n")

        if move == "help":
            I="(h)elp: see all possible actions \n"
            I+="(l)ocation: see current location \n"
            I+="(i)nfo: see all your stats \n"
            I+="e(x)amine + item: examine an item you possess \n"
            I+="(q)uit: leave the game \n"
            print(I)

        if move == "location" or move == "l":

            print("You are currently at: The " + P.pos +"\n")

        if move == "info" or move == "i":

            print(P)

        if move.split(" ")[0] == "examine" or move.split(" ")[0] == "x":
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i+" "

            Str=Str[:-1]

            if Str in P.items or Str==P.weapon or Str==P.armor:
                print(str(Item(Str))+"\n")

        if move == "quit" or move == "q":
            print("Thanks for having played my game!")
            exit()



        for event in self.events:

            if event.body==[False,False]:
                event.test(move,self)

            if event.body==[True,False]:
                event.run(move,self)

class Event:
    def __init__(self,name):
        self.name=name
        self.body=[False,False]

    def test(self,move,B):

        if self.name=="Start":

            if move == "start game":
                self.body[0]=True

    def run(self,move,B):

        if self.name=="Start":
            
            if B.enemies==[]:
                print("You see two marauding goblins approaching! \n")
                print("Type (a)ttack to fight them, before they get you! \n")

                B.enemies=[Enemy("Goblin1","Goblin"),Enemy("Goblin2","Goblin")]
