from Job import Job
from Item import Item

class Player:
    def __init__(self):
        self.job=None
        self.items=[]
        self.weapon=None
        self.armor=None
        self.consumables=[]
        self.specials=[]
        self.name=None
        self.pos="start"
        self.hp=None
        self.lv=1
        self.xp=0


        self.hpMax=None
        self.dmg=None

    def intro(self):
        print("Welcome to the game!")
        print("Here are the possible classes: \n")

        print(Job("Warrior"))
        print(Job("Wizard"))

        MyJob=input("Which class do you want to be? ")

        while Job(MyJob).dmg==None:
            print("Sorry, that isn't a possible class. \n")
            MyJob=input("Which class do you want to be? ")

        MyJob=Job(MyJob)

        self.job=MyJob.name
        self.dmg=MyJob.dmg
        self.hp=MyJob.hp
        self.hpMax=MyJob.hp
        self.items=[]
        for item in MyJob.items:
            if Item(item).mode=="weapon":
                self.weapon=item
            if Item(item).mode=="armor":
                self.armor=item
            if Item(item).mode=="consumable":
                self.consumables+=[item]
                self.items+=[item]

        print("\n")
        self.name = input("What is your character's name? ")
        print("\n")

        print("This is you: \n")
        print(self)

        print("Every turn you will type the action you want to preform.")
        print("Type 'start game' when you are ready to begin.")
        print("Type 'help' to see all possible moves. \n")

    def Up(self):
        self.xp-=2**(3+self.lv)
        self.lv+=1
        print("You are now level "+str(self.lv)+"!")
        print("Your damage increased by 5!")
        print("Your health increased by 10!\n")


    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Lv."+str(self.lv)+" "+self.job +"\n"
        I+= "Experience points: "+str(self.xp)+"/"+str(2**(2+self.lv))+"\n"
        I+= "Damage: "+str(self.dmg)+"\n"
        I+= "Health: "+str(self.hp)+"/"+str(self.hpMax)+"\n"
        I+= "Active Weapon: "+str(Item(self.weapon).name)+"\n"
        I+= "Active Armor: "+str(Item(self.armor).name)+"\n"
        I+= "Inventory: \n"
        for item in self.items:
            I+= "\t" + item + "\n"
        return I
        
