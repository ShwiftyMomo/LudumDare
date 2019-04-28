from Enemy import Enemy
from Item import Item
from King import King
from NPC import NPC

class Board:
    def __init__(self):
        self.enemies=[]
        self.events=[Event("Start"),Event("Forest"),Event("Clean Garden"),Event("Get Crown"),Event("Mountain"),Event("Ocean")]
        self.locations=["start","mountain","ocean","desert"]
        self.person=[]
        self.Done=True
        self.King=King()
        self.Gardener=NPC("Gardener")
        self.Blacksmith=NPC("Blacksmith")

    def turn(self,P):
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
                for people in self.person:
                    if not people.freind:
                        people.Attack(P)

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

            if move == "map" or move == "m":
                self.Map(P)

            if move == "spelunk" or move == "s":
                self.Spelunk(P)

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
            I+="(m)ap: show all locations \n"
            I+="(t)alk: talk to whoever is in your location \n"

        if self.events[4].body=[False,True]:
            I+="(s)pelunk: explore cave \n"

        print(I)
        self.Done=False

    def Location(self,P):
        print("You are currently at: The " + P.pos +"\n")
        self.Done=False

    def Attack(self,P):
        if self.enemies == [] and self.person == []:
            print("There are no enemies to attack." + "\n")

        else:
            I="Which enemy do you want to attack: \n"

            for enemy in self.enemies:
                I+="\t" + enemy.name +"\n"

            for people in self.person:
                I+="\t" + people.name +"\n"

            I+="\n"

            Enem = input(I)

            while Enem not in [enemy.name for enemy in self.enemies] and Enem not in [people.name for people in self.person]:
                print("That isin't one of the choices. \n")
                Enem = input(I)

            if Enem in [enemy.name for enemy in self.enemies]:
                Enem = self.enemies[[enemy.name for enemy in self.enemies].index(Enem)]

            if Enem in [people.name for people in self.person]:
                Enem=self.person[[people.name for people in self.person].index(Enem)]
                if Enem.freind:
                    print("You got "+Enem.name+" angry!")
                Enem.freind=False

            Enem.hp-=Item(P.weapon).dmg+P.dmg

            print("\n")
            print("You dealt " + Enem.name + " "+str(Item(P.weapon).dmg+P.dmg) + " damage!")

            if Enem.hp<=0:
                print("You killed " + Enem.name +"!")
                print("You got "+str(Enem.xp)+" experience points!")
                P.xp+=Enem.xp
                if P.xp>=2**(2+P.lv):
                    P.Up()

                if Enem in self.enemies:
                    self.enemies.remove(Enem)
                    if len(self.enemies)==0:
                        print("There are no more enemies left.")

                else:
                    self.person.remove(Enem)
                    if len(self.person)==0:
                        print("There are no NPCs left.")




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

                    if Str == "mountain":
                        self.person=[]
                        print("The mountain is tall and cold.")
                        if self.events[4].body==[False,False]:
                            self.events[4].body=[False,True]
                    if Str == "desert":
                        self.person=[]
                        print("The desert is hot and sweaty.")
                        print("There is a village of empoversihed goblins.")
                        print("The goblins are doing hard manual labor")

                    if Str == "forge":
                        self.person=[self.Blacksmith]
                        print("The forge is hot and fiery.")

                    if Str == "garden":
                        self.person=[self.Gardener]
                        print("The garden is nice are welcoming.")

                    if Str=="forest":
                        self.person=[self.King]
                        print("The forest is dark and gloomy.")

                    if Str=="start":
                        self.person=[]
                        print("You see an easter egg on the ground.")

                    self.Done=False

    def Talk(self,P):
        if len(self.person)==0:
            print("The walls do not seem to respond to your inquiry.")

        if len(self.person)==1:
            if self.person[0].freind:
                self.person[0].talk(P,self)
            else:
                print("You can't talk with enemies!")

        self.Done=False

    def Map(self,P):
        I="Locations: \n"
        for l in self.locations:
            I+="\t"+l+"\n"

        print(I)

    def Spelunk(self,P):
        if P.pos!="mountain":
            print("You must be near a cave to spelunk.")

        else:
            if "Dark Vision" not in P.specials:
                print("It is very dark, and you are hit by bats.")
                print("You get dealt 10 damage by the bats.")
                P.hp-=10
            else:
                print("You can see the bats with your Dark Vision.")
                print("You succesfully avoid the bats.")
                if "KILLER SWORD" != P.weapon and "KILLER SWORD" not in P.items:
                    print("You pick up a 'KILLER SWORD' at the back of the cave.")
                    P.items+=["KILLER SWORD"]

        print(I)

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
                B.locations+=["forest"]
                self.body=[False,True]

        if self.name=="Clean Garden":

            if B.enemies==[] and B.Gardener.stage==3:
                print("Gardener: Thank you for Cleaning my plants!")
                print("Gardener: As a reward, you can have my healing Potions!")
                P.consumables+=["Healing Potion","Healing Potion"]
                P.items+=["Healing Potion","Healing Potion"]
                self.body=[False,True]

        if self.name=="Get Crown":

            if B.enemies==[] and B.Blacksmith.stage==3:
                print("Blacksmith: I guess I'll give you the Crown now.")
                print("Blacksmith: As a bonus, I'll give you better gear.")
                print("Blacksmith: Type 'equip' then an item to make it your active item.")
                P.items+=["Medium Armor","Axe"]
                self.body=[False,True]

