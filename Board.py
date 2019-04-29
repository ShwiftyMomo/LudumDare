from Enemy import Enemy
from Item import Item
from King import King
from NPC import NPC
import time
class Board:
    def __init__(self):
        self.enemies=[]
        self.events=[Event("Start"),Event("Forest"),Event("Clean Garden"),Event("Get Crown")]
        self.events+=[Event("Mountain"),Event("Ocean"),Event("Goblin King")]
        self.locations=["start","desert"]
        self.person=[]
        self.Done=True
        self.King=King()
        self.Gardener=NPC("Gardener")
        self.Blacksmith=NPC("Blacksmith")
        self.Worker=NPC("Worker")

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

            if move == "quit" or move == "q":
                self.Quit(P)

            if move.split(" ")[0] == "use" or move.split(" ")[0] == "u":
                self.Use(P,move)

            if move == "walk" or move == "w":
                self.Walk(P)

            if move == "talk" or move == "t":
                self.Talk(P)

            if move == "spelunk" or move == "s":
                self.Spelunk(P)

            if move == "dive" or move == "d":
                self.Dive(P)

            if move.split(" ")[0] == "equip" or move.split(" ")[0] == "e":
                self.Equip(P,move)

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
        I+="(q)uit: leave the game \n"
        I+="(u)se + consumable: consume the consumable \n"
        I+="(e)quip + item: set item to your active item \n"
        if self.events[0].body!=[False,False]:
            I+="(w)alk: change location \n"
            I+="(t)alk: talk to whoever is in your location \n"

        if self.events[4].body==[False,True]:
            I+="(s)pelunk: explore cave \n"

        if self.events[5].body==[False,True]:
            I+="(d)ive: explore ocean \n"

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
            Temp=[]
            for word in Enem.split(" "):
                Temp+=[word[0].upper()+word[1:]]

            Enem=""
            for word in Temp:
                Enem+=word+" "

            Enem=Enem[:-1]

            while Enem not in [enemy.name for enemy in self.enemies] and Enem not in [people.name for people in self.person]:
                print("That isin't one of the choices. \n")
                Enem = input()
                Temp=[]
                for word in Enem.split(" "):
                    Temp+=[word[0].upper()+word[1:]]

                Enem=""
                for word in Temp:
                    Enem+=word+" "
                    
                Enem=Enem[:-1]

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
                Str+=i[0].upper()+i[1:]+" "

            Str=Str[:-1]

            if Str in P.items or Str==P.weapon or Str==P.armor:
                print(str(Item(Str))+"\n")
                self.Done=False

            if Str in [enemy.name for enemy in self.enemies]:
                print(str(self.enemies[[enemy.name for enemy in self.enemies].index(Str)])+"\n")
                self.Done=False

    def Quit(self,P):
        print("Thanks for having played my game!")
        self.Done=False
        exit()

    def Use(self,P,move):
        if len(move.split(" ")) !=1:
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i[0].upper()+i[1:]+" "

            Str=Str[:-1]

            if Str in P.consumables:
                P.consumables.remove(Str)
                P.items.remove(Str)

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

    def Walk(self,P):
        I="Locations: \n"
        for l in self.locations:
            I+="\t"+l+"\n"

        print(I)

        if self.enemies !=[]:
            print("You can't run away from a fight!")

        else:
            Enem=input().lower()

            while Enem not in self.locations:
                print("That isn't a possible location.")
                Enem=input().lower()

            P.pos=Enem
            print("You moved to the "+Enem+".")

            if Enem == "ocean":
                self.person=[]
                print("The ocean is large and blue.")
                if self.events[5].body==[False,False]:
                    self.events[5].body=[False,True]

            if Enem == "mountain":
                self.person=[]
                print("The mountain is tall and cold.")
                if self.events[4].body==[False,False]:
                    self.events[4].body=[False,True]
            if Enem == "desert":
                self.person=[self.Worker]
                print("The desert is hot and sweaty.")
                print("There is a Worker goblin hard at work")

            if Enem == "forge":
                print("The forge is hot and fiery.")
                if self.Blacksmith.hp>0:
                    self.person=[self.Blacksmith]
                    print("There is a Blacksmith hard at work")
                else:
                    self.person=[]

            if Enem == "garden":
                print("The garden is nice are welcoming.")
                if self.Gardener.hp>0:
                    self.person=[self.Gardener]
                    print("There is a Gardener tending to their plants.")
                else:
                    self.person=[]
            if Enem=="forest":
                self.person=[self.King]
                print("The forest is dark and gloomy.")

            if Enem=="start":
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

    def Spelunk(self,P):
        if P.pos!="mountain":
            print("You must be near a cave to spelunk.")

        else:
            if "Dark Vision" not in P.specials:
                print("It is very dark, and you are hit by bats.")
                print("You get dealt 10 damage by the bats.")
                P.hp-=10
                if P.hp<=0:
                    P.die()
            else:
                print("You can see the bats with your Dark Vision.")
                print("You succesfully avoid the bats.")
                if "KILLER SWORD" != P.weapon and "KILLER SWORD" not in P.items:
                    print("You pick up a 'KILLER SWORD' at the back of the cave.")
                    P.items+=["KILLER SWORD"]

        self.Done=False

    def Equip(self,P,move):
        if len(move.split(" ")) !=1:
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i[0].upper()+i[1:]+" "

            Str=Str[:-1]

            if Str in P.items:
                if Item(Str).mode=="weapon":
                    P.items+=[P.weapon]
                    P.items.remove(Str)
                    P.weapon=Str
                    print("You equiped '"+Str+"'!")

                if Item(Str).mode=="armor":
                    P.items+=[P.armor]
                    P.items.remove(Str)
                    P.armor=Str
                    print("You equiped '"+Str+"'!")

                if Item(Str).mode=="consumable":
                    print("You cannot equip consumables")

                self.Done=False

    def Dive(self,P):
        if P.pos!="ocean":
            print("You must be near a body of water to dive.")

        else:
            if "Water Breathing" not in P.specials:
                print("It is very deep, and you run out of air.")
                print("You get lightheaded and lose 10 hp.")
                P.hp-=10
                if P.hp<=0:
                    if P.job!="Bard":
                        P.die()
                    else:
                        time.sleep(1)
                        print("Desire and")
                        time.sleep(1)
                        print("All the sweet pulsing aches")
                        time.sleep(1)
                        print("and gentle hurtings")
                        time.sleep(1)
                        print("That were you,")
                        time.sleep(1)
                        print("Are gone into the sullen dark.")
                        time.sleep(1)
                        print("--Ernest Hemmingway")
                        time.sleep(1)
                        print("\n")
                        time.sleep(5)
                        print("WAIT!")
                        time.sleep(1)
                        print("A group of Mer-People save you.")
                        print("It turns out Atlantis has a Bard shortage.")
                        time.sleep(1)
                        print("Epilogue:")
                        time.sleep(3)
                        print("You live with the Mer-people for the rest of eternity.")
                        time.sleep(3)
                        print("Are you dead or is this happening?")
                        time.sleep(3)
                        print("And is there a difference?")
                        time.sleep(3)
                        exit()
            else:
                print("You can survive with your Water Breathing.")
                print("You succesfully swim to the bottom of the ocean.")
                if "Friendship Bracelet" != P.weapon and "Friendship Bracelet" not in P.items:
                    print("You pick up a 'Friendship Bracelet' at the bottom of the ocean.")
                    P.items+=["Friendship Bracelet"]

        self.Done=False

    def ending(self):
        print("\n")
        print("The goblin king has a matching freindship bracelet!")
        time.sleep(3)
        print("Goblin King: That... That's my best freind's bracelet.")
        time.sleep(3)
        print("The Goblin King gives you a big hug.")
        time.sleep(3)
        print("Epilogue:")
        time.sleep(3)
        print("You and the Goblin King become BFFs.")
        time.sleep(3)
        print("But not all is good.")
        time.sleep(3)
        print("The conditions in the goblin village haven't gotten better.")
        time.sleep(3)
        print("And the Goblin King still calls the Gardener stinky.")
        time.sleep(3)
        print("You may have saved this one soul...")
        time.sleep(3)
        print("...but was it worth not helping the village?")
        time.sleep(3)
        exit()


class Event:
    def __init__(self,name):
        self.name=name
        self.body=[False,False]

    def test(self,move,B,P):

        if self.name=="Start":

            if move == "start game":
                self.body[0]=True

                print("You see two marauding goblins approaching! \n")
                print("Type '(a)ttack' to fight them, before they get you!")

                B.enemies=[Enemy("Goblin1","Goblin"),Enemy("Goblin2","Goblin")]

                B.Done=False

        if self.name=="Forest":

            if P.pos=="forest":
                self.body[0]=True

                print("A large figure approaches you.")
                print("Goblin King: I am the king of these lands.")
                print("Goblin King: If you wish to stay alive, you must complete my quests.")
                print("Type '(t)alk' to talk whoever is in your location. \n")

        if self.name=="Goblin King":

            if B.King.hp<=0:
                print("You have defeated the Goblin King!")
                time.sleep(5)
                print("Epilogue:")
                time.sleep(3)
                print("The goblin village has gotten a bit better.")
                time.sleep(3)
                print("But it is slightly melancholic.")
                time.sleep(3)
                print("You have killed the king, but for what.")
                time.sleep(3)
                print("All he ever wanted was a friend.")
                time.sleep(3)
                print("He had started to think that maybe you were a friend.")
                time.sleep(3)
                print("You think that he needed you to go on those quests?")
                time.sleep(3)
                print("No.")
                time.sleep(3)
                print("He just wanted to build a friendship.")
                time.sleep(3)
                print("And you killed him.")
                time.sleep(3)
                print("I hope you're happy with you 'decision'.")
                time.sleep(3)
                exit()
    def run(self,move,B,P):

        if self.name=="Start":

            if B.enemies==[]:

                print("Congratulations, you fended off the Goblins!")
                print("They came from the forest up above, so you might want to go check that out.")
                print("Type '(w)alk' to go to the forest. \n")
                B.locations+=["forest"]
                self.body=[False,True]

        if self.name=="Clean Garden":

            if B.enemies==[] and B.Gardener.stage==3:
                print("Gardener: Thank you for Cleaning my plants!")
                print("Gardener: As a reward, you can have my healing Potions!")
                P.consumables+=["Healing Potion","Healing Potion"]
                P.items+=["Healing Potion","Healing Potion"]
                print("You have completed the 'Clean Garden' quest!")
                self.body=[False,True]

        if self.name=="Get Crown":

            if B.enemies==[] and B.Blacksmith.stage==3:
                print("Blacksmith: I guess I'll give you the Crown now.")
                print("Blacksmith: As a bonus, I'll give you better gear.")
                print("Blacksmith: Type '(b)estow' then an item to make it your active item.\n")
                B.locations+=["mountain"]
                P.items+=["Medium Armor","Axe"]
                print("You have completed the 'Get Crown' quest!")
                self.body=[False,True]

