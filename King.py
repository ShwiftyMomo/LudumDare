from Player import Player

class King:
	def __init__(self):
		self.deals=["Strengh"]
		self.quests=["Clean Garden"]

	def talk(self,P,B):
		print("Goblin King: Here are my quests \n")
		for quest in self.quests:
			print("--"+quest+"--")

		print("\n")
		print("Goblin King: Here are my pacts \n")
		for deal in self.deals:
			print(Pact(deal))

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

class Pact:
	def __init__(self,name):
		self.name=name

		if name == "Strengh":
			self.cost=25
			self.blurb="Increase strength"
	
	def run(self,P):
		P.hpMax-=self.cost
		if P.hp>P.hpMax:
			P.hp=P.hpMax

		if self.name == "Strengh":
			P.dmg+=15

	def __str__(self):
		I= "--"+self.name+"-- \n"
		I+= "Cost: "+str(self.cost)+"\n"
		I+= "Effect: "+self.blurb+"\n"
		return I

