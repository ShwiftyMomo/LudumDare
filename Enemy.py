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



    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Damage Dealt: "+str(self.hpMax-self.hp)+"\n"
        return I
