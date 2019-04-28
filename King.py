from Player import Player
from Item import Item
class King:
	def __init__(self):
		self.name = "Goblin King"
		self.deals=["Strength","Water Breathing"]
		self.quests=["Clean Garden"]
		self.freind=True
		self.hp=300
		self.dmg=50
		self.xp=100

	def talk(self,P,B):
		if self.Events[2]==[False,True]:
			print("Goblin King: Back for another quest I see")

		print("Goblin King: Here are my quests \n")
		for quest in self.quests:
			print("--"+quest+"--")

		print("\n")
		print("Goblin King: Here are my pacts \n")
		for deal in self.deals:
			print(Pact(deal))
			print("")

		print("Goblin King: Type the name of the quest/pact you want.")
		print("Goblin King: Or just move on if you dont want anything.\n")
		move=input()

		if move in self.deals:
			Pact(move).run(P)
			print("You got the pact '"+move+"'!")

		if move in self.quests:

			if move=="Clean Garden":
				B.events[2].body[0]=True

			self.quests.remove(move)

			print("You have decided to embark on the '"+move+"' quest!\n")
			B.locations+=["garden"]

		B.events[1].body=[False,True]

	def Attack(self,P):
		print(self.name + " dealt you "+str(int(self.dmg/Item(P.armor).arm))+" damage.")
		P.hp-=int(self.dmg/Item(P.armor).arm)
		if P.hp<=0:
			print(self.name +" has killed you!\n")
			P.die()

class Pact:
	def __init__(self,name):
		self.name=name

		if name == "Strength":
			self.cost=25
			self.blurb="Increase strength"

		if name == "Water Breathing":
			self.cost=25
			self.blurb="Be able to breathe undervater"
	
	def run(self,P):
		P.hpMax-=self.cost

		if P.hp>P.hpMax:
			P.hp=P.hpMax

		if self.name == "Strength":
			P.dmg+=30

		if self.name == "Water Breathing":
			P.specials+=["Water Breathing"]

	def __str__(self):
		I= "--"+self.name+"-- \n"
		I+= "Cost: "+str(self.cost)+"\n"
		I+= "Effect: "+self.blurb+"\n"
		return I

