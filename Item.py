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