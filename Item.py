class Item:
    def __init__(self,mode):
        self.name=mode

        if mode=="Sword":
            self.dmg=20
            self.blurb="The original, a sword."
            self.mode="weapon"

        if mode=="Light Armor":
            self.arm=10
            self.blurb="A wee bit of protection is better than none at all."
            self.mode="armor"

        if mode=="Healing Potion":
            self.effect=["hp",50]
            self.blurb="Recovering health is quite important when at 1 hp."
            self.mode="consumable"

        if mode=="Sword":
            self.dmg=20
            self.blurb="The original, a sword."
            self.mode="weapon"

        if mode=="Magic Wand":
            self.dmg=45
            self.blurb="Doin' it Harry Potter style."
            self.mode="weapon"

        if mode=="Robes":
            self.arm=10
            self.blurb="Honestly, im not sure if it counts as real armor."
            self.mode="armor"

    def __str__(self):
        I= "--"+self.name+"-- \n"

        I+="Type: "+str(self.mode)+"\n"

        if self.mode== "weapon":
            I+= "Damage: "+str(self.dmg)+"\n"

        if self.mode == "armor":
            I+= "Defence: "+str(self.arm)+"\n"

        if self.mode == "consumable":
            I+="This consumable "

            if self.effect[1]>0:
                I+="increases "

            if self.effect[1]<0:
                I+="decreases "

            I+= self.effect[0]+ " by "+str(abs(self.effect[1]))+"\n"

        I+=self.blurb
        return I

