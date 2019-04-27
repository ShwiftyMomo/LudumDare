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