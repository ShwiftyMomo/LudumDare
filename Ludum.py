class Item:
    def __init__(self,name,effect,blurb,mode):
        self.name=name
        self.dmg=None
        self.arm=None
        self.effect=None
        self.blurb=blurb
        self.mode=mode

        if mode=="weapon":
            self.dmg=effect
        if mode=="armor":
            self.arm=effect
        if mode=="consumable":
            self.effect=effect

    def __str__(self):
        I= "--"+self.name+"-- \n"

        I+="Type: "+str(self.mode)+"\n"

        if self.mode== "weapon":
            I+= "Damage: "+str(self.dmg)+"\n"

        if self.mode == "armor":
            I+= "Defence: "+str(self.hp)+"\n"

        if self.mode == "consumable":
            I+="This consumable"

            if self.effect[1]>0:
                I+="increases "

            if self.effect[1]<0:
                I+="decreases "

            I+= self.effect[0]+ " by "+str(abs(self.effect[1]))+"\n"

        I+=self.blurb
        return I

class Job:
    def __init__(self,name,dmg,hp,items):
        self.name=name
        self.dmg=dmg
        self.hp=hp
        self.items=items

    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Damage: "+str(self.dmg)+"\n"
        I+= "Health: "+str(self.hp)+"\n"
        I+= "Starting Items: \n"
        for item in self.items:
            I+= "\t" + item + "\n"
        return I

class Player:
    def __init__(self):
        self.job=None
        self.items=[]
        self.weapon=None
        self.armor=None
        self.consumables=[]
        self.specials=[]
        self.name=None
        self.pos="Start"
        self.hp=None
        self.hpMax=None
        self.dmg=None

    def intro(self):
        print("Welcome to the game!")
        print("Here are the possible classes: \n")

        for job in Jobs:
            print(job)

        MyJob=input("Which class do you want to be? ")

        while MyJob not in [J.name for J in Jobs]:
            print("Sorry, that isn't a possible class. \n")
            MyJob=input("Which class do you want to be? ")

        MyJob=Jobs[[J.name for J in Jobs].index(MyJob)]

        MyJobItems=[Items[[item.name for item in Items].index(I)] for I in MyJob.items]
        self.job=MyJob.name
        self.dmg=MyJob.dmg
        self.hp=MyJob.hp
        self.hpMax=MyJob.hp
        self.items=MyJobItems
        for item in MyJobItems:
            if item.mode=="weapon":
                self.weapon=item
            if item.mode=="armor":
                self.armor=item
            if item.mode=="consumable":
                self.consumables+=[item]

        print("\n")
        self.name = input("What is your character's name? ")
        print("\n")

        print("This is you: \n")
        print(self)

        print("Every turn you will type the action you want to preform.")
        print("Type 'help' to see all possible moves. \n")



    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Damage: "+str(self.dmg)+"\n"
        I+= "Health: "+str(self.hp)+"/"+str(self.hpMax)+"\n"
        I+= "Items: \n"
        for item in self.items:
            I+= "\t" + item.name + "\n"
        return I

class Enemy:
    def __init__(self,name,dmg,hp,items):
        self.name=name
        self.dmg=dmg
        self.hpMax=hp
        self.hp=hp
        self.items=items

    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Damage Dealt: "+str(self.hpMax-self.hp)+"\n"
        return I

class Board:
    def __init__(self):
        self.enemies=[]

    def turn(self,P):
        move=input()
        print("\n")

        if move == "help":
            I="help: see all possible actions \n"
            I+="location: see current location \n"
            I+="info: see all your stats \n"
            I+="examine + item: examine an item you possess \n"
            print(I)

        if move == "location":
            print(P.pos +"\n")

        if move == "info":
            print(P)

        if move.split(" ")[0] == "examine":
            Str=""
            for i in move.split(" ")[1:]:
                Str+=i

            item=P.items[[item.name for item in P.items].index(Str)]

            print(item)

        if move == "exit":
            print("Thanks for playing my game!")
            Running=False

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
