class Job:
    def __init__(self,part):
        self.name=None
        self.dmg=None
        self.hp=None
        self.items=["Easter Egg"]

        if part=="warrior":
            self.name="Warrior"
            self.dmg=25
            self.hp=125
            self.items=["Sword","Healing Potion","Light Armor"]

        if part=="wizard":
            self.name="Wizard"
            self.dmg=10
            self.hp=75
            self.items=["Magic Wand","Healing Potion","Robes"]

        if part=="bard":
            self.name="Bard"
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
