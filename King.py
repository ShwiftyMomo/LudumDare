from Player import Player
from Item import Item
class King:
	def __init__(self):
		self.name = "Goblin King"
		self.deals=["Strength","Water Breathing","Dark Vision"]
		self.quests=["Clean Garden","Get Crown"]
		self.freind=True
		self.hp=10000
		self.dmg=100
		self.xp=1000

	def talk(self,P,B):

		if P.weapon=="Friendship Bracelet":
			B.ending()

		if B.events[2].body==[False,True] or B.events[3].body==[False,True]:
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

		move = input()

		if move!="":
			Temp=[]
			for word in move.split(" "):
				Temp+=[word[0].upper()+word[1:]]

			move=""

			for word in Temp:
				move+=word+" "

			move=move[:-1]

			if move in self.deals:
				Pact(move).run(P)
				print("You got the pact '"+move+"'!")

			if move in self.quests:

				if move=="Clean Garden":
					B.events[2].body[0]=True
					B.locations+=["garden"]
					self.quests.remove("Clean Garden")
					print("You have decided to embark on the 'Clean Garden' quest!\n")

				if move=="Get Crown":
					B.events[3].body[0]=True
					B.locations+=["forge"]
					self.quests.remove("Get Crown")
					print("You have decided to embark on the 'Get Crown' quest!\n")

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
			self.blurb="Be able to breathe underwater"

		if name == "Dark Vision":
			self.cost=25
			self.blurb="Be able to see in the dark"
	
	def run(self,P):
		P.hpMax-=self.cost

		if P.hp>P.hpMax:
			P.hp=P.hpMax

		if self.name == "Strength":
			P.dmg+=30

		if self.name == "Water Breathing":
			P.specials+=["Water Breathing"]

		if self.name == "Dark Vision":
			P.specials+=["Dark Vision"]

	def __str__(self):
		I= "--"+self.name+"-- \n"
		I+= "Cost: "+str(self.cost)+"\n"
		I+= "Effect: "+self.blurb+"\n"
		return I

