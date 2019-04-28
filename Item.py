class Item:
    def __init__(self,mode):
        self.name=mode
        self.dmg=-1
        self.arm=-1
        self.blurb="Blurb"
        self.mode="Mode"
        self.effect=["Word",0]

        if mode=="Sword":
            self.dmg=20
            self.blurb="The original, a sword."
            self.mode="weapon"

        if mode=="Lute":
            self.dmg=15
            self.blurb="A musical instrument."
            self.mode="weapon"

        if mode=="Freindship Bracelet":
            self.dmg=20
            self.blurb="It says Goblin + Bobby forever."
            self.mode="weapon"

        if mode=="KILLER SWORD":
            self.dmg=1000000
            self.blurb="This masterwork sword can kill anything."
            self.mode="weapon"

        if mode=="Axe":
            self.dmg=20
            self.blurb="A two-sided head chopper."
            self.mode="weapon"

        if mode=="Mass":
            self.dmg=10
            self.blurb="An overwhelming force."
            self.mode="weapon"

        if mode=="Light Armor":
            self.arm=1.3
            self.blurb="A wee bit of protection is better than none at all."
            self.mode="armor"

        if mode=="Medium Armor":
            self.arm=1.5
            self.blurb="Hefty protection."
            self.mode="armor"

        if mode=="Healing Potion":
            self.effect=["hp",50]
            self.blurb="Recovering health is quite important when at 1 hp."
            self.mode="consumable"

        if mode=="Knife":
            self.dmg=10
            self.blurb="A small shank. For shanking purposes."
            self.mode="weapon"

        if mode=="Magic Wand":
            self.dmg=45
            self.blurb="Doin' it Harry Potter style."
            self.mode="weapon"

        if mode=="Robes":
            self.arm=1.1
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

