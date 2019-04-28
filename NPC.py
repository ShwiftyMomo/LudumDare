from Player import Player
from Item import Item

class NPC:
	def __init__(self,name):
		self.name = name
		self.freind=True
		self.stage=1
		if name=="Gardener":
			self.hp=125
			self.dmg=5
			self.xp=15

	def ask(self,Questions):
		I=""
		for i in range(len(Questions)):
			I+="\t"+str(i+1)+") "+Questions[i]+"\n"

		Enem=input(I)
		Temp=True
		if type(Enem)==int:
			if not(int(Enem)-1 in range(len(Questions))):
				Temp=False
		while Temp:
			print("Please enter the number of the option you wish to chose. \n")
			Enem=input(I)

			try:
				if int(Enem)-1 in range(len(Questions)):
					Temp=False
			except ValueError as e:
				pass

		return int(Enem)

	def talk(self,P,B):
		if self.name=="Gardener":
			if self.stage ==1 or self.stage ==2:

					if self.stage ==1:
						self.stage=2
						print("Gardener: Oh, a new face!")
						print("Gardener: It was getting boring with just my dirty plants.")

					if self.stage ==2:
						print("Gardener: What do you want to talk about?")

					O1="Why are your plants dirty?"
					O2="What's up with the Goblin King?"
					O3="What is the meaning of life?"
					Op1=self.ask([O1,O2,O3])

					if Op1==1:
						print("Gardener: A couple of mandrakes made my garden their home.")
						O1="I'll deal with them."
						O2="Neato."
						Op2=self.ask([O1,O2])

						if Op2==1:
							print("As if on que, a horde of mandrakes jump out of the dirt.")
							B.enemies+=[Enemy("Mandrake Horde","Horde")]
							self.stage=3

					if Op1==2:
						print("Gardener: I think he's overcompensating for a lack of close freinships.")
						print("Gardener: Perhaps you could become his freind and heal the hole in his heart.")
						O1="How could I befreind him?"
						O2="Have you tried befreinding him yourself?"
						O3="Cool."
						Op2=self.ask([O1,O2,O3])


						if Op2==1:
							print("Gardener: The Goblin King used to have a best freind...")
							print("Gardener: But one day when they were out at sea their ship sunk.")
							print("Gardener: You would need to find a way to replace them.")

						if Op2==2:
							print("Gardener: He thinks i'm stinky")
							O1="I would tend to agree with the Goblin on this one."
							O2="Well isn't that just rude."
							Op2=self.ask([O1,O2])

					if Op1==3:
						print("Gardener: One could argue life has no inherent meaning.")
						print("Gardener: Perhaps one needs a god to beleive life has meaning.")
						print("Gardener: What do you think?")

						O1="Are suggesting athiests don't have meaning in their lives?"
						O2="Honestly, that's something I've always asked myself."
						O3="To reproduce, speaking evolutionarily."
						O4="To maximise happyness."
						O5="We can all chose our own meaning for live."
						O6="Dude, I asked you first."
						Op2=self.ask([O1,O2,O3,O4,O5,O6])

						if Op2==1:
							print("Gardener: I'm saying athiests don't beleive they have meaning in their lives.")
							print("Gardener: Theists don't have meaning if God does not exist, even if they beleive.")

						if Op2==3:
							print("Gardener: Would it then follow that those who do not reproduce have no meaning?")
							O1="I suppose it would."
							O2="Not having meaning isin't neccecarily a bad thing."
							O3="You're twisting my words here goddamit."
							O4="Whatever."
							Op3=self.ask([O1,O2,O3,O4])

							if Op3==1 or Op3==2:
								print("Gardener: This would explain why people so primaly fear regection.")
								print("Gardener: Have you ever been regected?")
								O1="No."
								O2="Yes, once."
								O3="Alas, regection has become the norm for me."
								Op4=self.ask([O1,O2,O3])

								if Op4==1:
									print("Gardener: Lucky.")

								if Op4==2 or Op4==3:
									print("Gardener: Getting over them is hard.")
									print("Gardener: But you just gotta keep going.")
									print("Gardener: Keep on trying.")
									print("Gardener: Keep on living.")
									print("Gardener: Keep on loving.")
									print("Gardener: Despite how impossible it might feel.")


							if Op3==3:
								print("Gardener: I meerly restated your argument back at you.")

							if Op3==4:
								print("Gardener: Ignoring something does not make it go away")

						if Op2==4:
							print("Gardener: You must then ask yourself if what you're doing with your life makes you truly happy.")
							print("Gardener: Or if it's all just momentary and supperficial.")
							print("Gardener: Or if what you do makes you happy at all.")

						if Op2==5:
							print("Gardener: So the  'universal' meaning of live is to succeed in our own hyper personal meanings?")
							O1="I suppose."
							O2="Many would have the same meanings, so it wouldn't be 'hyper-personal'."
							Op3=self.ask([O1,O2])

							print("Gardener: What would you meaning be?")
							O1="To live."
							O2="To love."
							O3="To survive."
							O4="To be happy."
							O5="To die."
							Op3=self.ask([O1,O2,O3,O4,O5])

							if Op3==5:
								print("Gardener: Would you lose your meaning if you became immortal?")
								O1="I would get a new meaning."
								O2="Yes."
								O3="Dude, that's deep."
								Op3=self.ask([O1,O2,O3])
			
	def Attack(self,P):
		print(self.name + " dealt you "+str(int(self.dmg/Item(P.armor).arm))+" damage.")
		P.hp-=int(self.dmg/Item(P.armor).arm)
		if P.hp<=0:
			print(self.name +" has killed you!\n")
			P.die()