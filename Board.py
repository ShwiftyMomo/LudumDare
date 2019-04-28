from Enemy import Enemy
from Item import Item
from King import King

class Board:
    def __init__(self):
        self.enemies=[]
        self.events=[Event("Start"),Event("Forest"),Event("Clean Garden")]
        self.locations=["start","forest"]
        self.Done=True

    def turn(self,P,K):
        print("\n")

        self.Done=True
        while self.Done:

            move=input("Your move: ")
            print("\n")

            if move == "help" or move == "h":
                self.Help(P)
            if move == "location" or move == "l":
                self.Location(P)

            if move == "attack" or move == "a":
                self.Attack(P)
                for enemy in self.enemies:
                    enemy.Attack(P)

            if move == "info" or move == "i":
                self.Info(P)

            if move.split(" ")[0] == "examine" or move.split(" ")[0] == "x":
                self.Examine(P,move)

            if move == "exit" or move == "e":
                self.Exit(P)

            if move.split(" ")[0] == "use" or move.split(" ")[0] == "u":
                self.Use(P,move)

            if move.split(" ")[0] == "walk" or move.split(" ")[0] == "w":
                self.Walk(P,move)

            if move == "talk" or move == "t":
                self.Talk(P)

            for event in self.events:

                if event.body==[False,False]:
                    event.test(move,self,P)

                if event.body==[True,False]:
                    event.run(move,self,P)

            if self.Done:
                print("That is not a valid move, please try again")

    def Help(self,P):
        I="(h)elp: see all possible actions \n"
        I+="(l)ocation: see current location \n"
        I+="(i)nfo: see all your stats \n"
        I+="e(x)amine + item: examine an item you possess \n"
        I+="e(x)amine + enemy: examine an enemy you are fighting \n"
        I+="(a)ttack: attack enemies \n"
        I+="(e)xit: leave the game \n"
        I+="(u)se + consumable: consume the consumable \n"
        if self.events[0].body!=[False,False]:
            I+="(w)alk + location: change location \n"
        if self.events[1].body!=[False,False]:
            I+="(t)alk: talk to whoever is in your location \n"
        print(I)
        self.Done=False

    def Location(self,P):
        print("You are currently at: The " + P.pos +"\n")
        self.Done=False

    def Attack(self,P):
        if self.enemies == []:
            print("There are no enemies to attack." + "\n")

        else:
            I="Which enemy do you want to attack: \n"

            for enemy in self.enemies:
                I+="\t" + enemy.name +"\n"

            I+="\n"

            Enem = input(I)

            while Enem not in [enemy.name for enemy in self.enemies]:
                print("That isin't one of the choices. \n")
                Enem = input(I)

            Enem = self.enemies[[enemy.name for enemy in self.enemies].index(Enem)]

            Enem.hp-=Item(P.weapon).dmg+P.dmg

            print("\n")
            print("You dealt " + Enem.name + " "+str(Item(P.weapon).dmg+P.dmg) + " damage!")

            if Enem.hp<=0:
                print("You killed " + Enem.name +"!")
                print("You got "+str(Enem.xp)+" experience points!")
                P.xp+=Enem.xp
                if P.xp>=2**(2+P.lv):
                    P.Up()
                self.enemies.remove(Enem)


            if len(self.enemies)==0:
                print("There are no more enemies left.")

            print("\n")

        self.Done=False

    def Info(self,P):
        print(P)
        self.Done=False

    def Examine(self,P,move):
        if len(move.split(" ")) !=1:
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i+" "

            Str=Str[:-1]

            if Str in P.items or Str==P.weapon or Str==P.armor:
                print(str(Item(Str))+"\n")
                self.Done=False

            if Str in [enemy.name for enemy in self.enemies]:
                print(str(self.enemies[[enemy.name for enemy in self.enemies].index(Str)])+"\n")
                self.Done=False

    def Exit(self,P):
        print("Thanks for having played my game!")
        self.Done=False
        exit()

    def Use(self,P,move):
        if len(move.split(" ")) !=1:
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i+" "

            Str=Str[:-1]

            if Str in P.consumables:
                P.consumables.remove(Str)

                if Item(Str).effect[0]=="hp":
                    I="hp"

                    num=Item(Str).effect[1]

                    P.hp+=num

                    if P.hp>P.hpMax:
                        P.hp=P.hpMax

                if Item(Str).effect[0]=="hpMax":
                    I="Maximum hp"

                    num=Item(Str).effect[1]

                    P.hpMax+=num

                if num>0:
                    I+=" increased by "

                if num<0:
                    I+=" decreased by "

                I+= str(abs(num))

                I+="."

                print(I)

                self.Done=False

    def Walk(self,P,move):
        if len(move.split(" ")) !=1:
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i+" "

            Str=Str[:-1]

            if Str in self.locations:
                if self.enemies !=[]:
                    print("You can't run away from a fight!")

                else:
                    P.pos=Str
                    print("You moved to the "+Str+".")
                    self.Done=False

    def Talk(self,P):
        King().talk(P,self)
        self.Done=False

class Event:
    def __init__(self,name):
        self.name=name
        self.body=[False,False]

    def test(self,move,B,P):

        if self.name=="Start":

            if move == "start game":
                self.body[0]=True

                print("You see two marauding goblins approaching! \n")
                print("Type 'attack' to fight them, before they get you!")

                B.enemies=[Enemy("Goblin1","Goblin"),Enemy("Goblin2","Goblin")]

                B.Done=False

        if self.name=="Forest":

            if P.pos=="forest":
                self.body[0]=True

                print("The forest is dark and gloomy.")
                print("A large figure approaches you.")
                print("Goblin King: I am the king of these lands.")
                print("Goblin King: If you wish to stay alive, you must complete my quests.")
                print("Type 'talk' to talk whoever is in your location. \n")


    def run(self,move,B,P):

        if self.name=="Start":

            if B.enemies==[]:

                print("Congratulations, you fended off the Goblins!")
                print("They came from the forest up above, so you might want to go check that out.")
                print("Type 'walk forest' to go to the forest. \n")

                self.body=[False,True]
