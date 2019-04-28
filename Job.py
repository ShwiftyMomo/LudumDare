class Job:
    def __init__(self,part):
        self.name=part
        self.dmg=None
        self.hp=None
        self.items=["Easter Egg"]
        if part=="Warrior":
            self.dmg=25
            self.hp=125
            self.items=["Sword","Healing Potion","Light Armor"]

        if part=="Wizard":
            self.dmg=10
            self.hp=75
            self.items=["Magic Wand","Healing Potion","Robes"]

        if part=="Bard":
            self.dmg=10
            self.hp=50
            self.items=["Lute","Healing Potion","Robes"]



    def __str__(self):
        I= "--"+self.name+"-- \n"
        I+= "Damage: "+str(self.dmg)+"\n"
        I+= "Health: "+str(self.hp)+"\n"
        I+= "Starting Items: \n"
        for item in self.items:
            I+= "\t" + item + "\n"
        return I
