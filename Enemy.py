from Item import Item
class Enemy:
    def __init__(self,name,part):
        self.name=name

        if part == "Goblin":
            self.dmg=0
            self.hpMax=75
            self.hp=75
            self.weapon="Knife"

        if part == "Orc":
            self.dmg=0
            self.hpMax=125
            self.hp=125
            self.weapon="Knife"


        if part == "Mercenary":
            self.dmg=0
            self.hpMax=100
            self.hp=100
            self.weapon="Sword"


    def attack(self,P):
        print(self.name + " dealt you "+str(int((self.dmg+Item(self.weapon).dmg)/Item(P.armor).arm))+" damage.")
        P.hp-=int((self.dmg+Item(self.weapon).dmg)/Item(P.armor).arm)

    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Damage Dealt: "+str(self.hpMax-self.hp)+"\n"
        return I
