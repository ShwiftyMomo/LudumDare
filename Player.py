from Job import Jobs
from Item import Items

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
        self.items=[]
        for item in MyJobItems:
            if item.mode=="weapon":
                self.weapon=item
            if item.mode=="armor":
                self.armor=item
            if item.mode=="consumable":
                self.consumables+=[item]
                self.items+=[item]

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
        I+= "Active Weapon: "+str(self.weapon.name)+"\n"
        I+= "Active Armor: "+str(self.armor.name)+"\n"
        I+= "Inventory: \n"
        for item in self.items:
            I+= "\t" + item.name + "\n"
        return I
        