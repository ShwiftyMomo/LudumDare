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