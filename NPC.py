from Player import Player
from Item import Item
from Enemy import Enemy
class NPC:
	def __init__(self,name):
		self.name = name
		self.freind=True
		self.stage=1
		if name=="Gardener":
			self.hp=125
			self.dmg=5
			self.xp=15

		if name=="Blacksmith":
			self.hp=150
			self.dmg=5
			self.xp=25

		if name=="Worker":
			self.hp=50
			self.dmg=5
			self.xp=10

	def ask(self,Questions):
		I=""
		for i in range(len(Questions)):
			I+="\t"+str(i+1)+") "+Questions[i]+"\n"

		Enem=input(I)
		Temp=True
		try:
			if int(Enem)-1 in range(len(Questions)):
				Temp=False
		except ValueError as e:
			pass
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

			if self.stage ==1:
				self.stage=2
				print("Gardener: Oh, a new face!")
				print("Gardener: It was getting boring with just my dirty plants.")

			if self.stage ==2 or self.stage ==3:
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
					print("As if on queue, a horde of mandrakes jump out of the dirt.")
					B.enemies+=[Enemy("Mandrake Horde","Horde")]
					self.stage=3

			if Op1==2:
				print("Gardener: I think he's overcompensating for a lack of close friendships.")
				print("Gardener: Perhaps you could become his freind and heal the hole in his heart.")
				O1="How could I befreind him?"
				O2="Have you tried befreinding him yourself?"
				O3="Cool."
				Op2=self.ask([O1,O2,O3])


				if Op2==1:
					print("Gardener: The Goblin King used to have a best friend...")
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

		if self.name=="Blacksmith":
			if self.stage ==1:
				self.stage=2
				print("Blacksmith: Haven't seen you around here.")
				print("Blacksmith: What you here for?")

			if self.stage ==2 or self.stage ==3:
				print("Blacksmith: You got something to say?")

			O1="Could I get a crown for the Goblin King?"
			O2="How could I, say, kill the Goblin King?"
			O3="Do us humans have free will?"
			Op1=self.ask([O1,O2,O3])

			if Op1==1:
				print("Blacksmith: Oh, that's what your here for.")
				print("Blacksmith: When making it for him I dropped it in a pit of spiders.")
				print("Blacksmith: So you'll have to deal with that.")

				O1= "Oh HELL no. I'm an arachnophobe."
				O2= "Well... I'll do it anyway."
				O3= "Dude, I eat spiders for breakfast"
				Op2=self.ask([O1,O2,O3])

				if Op2==2 or Op2==3:
					print("Blacksmith: Well it's your lucky day then.")
					print("A horde of spiders come out of the pit to fight you.")
					B.enemies+=[Enemy("Spider Den","Horde")]
					self.stage=3

			if Op1==2:
				print("Blacksmith: I once forged a blade that could kill any goblin it touched...")
				print("Blacksmith: But I went backpacking and lost it.")
				print("Blacksmith: You could try to find it, I guess.")

				O1="Goddamit."
				O2="Where did you lose it?"
				O3="Sounds like a 'you' problem."
				Op2=self.ask([O1,O2,O3])

				if Op2==2:
					print("Blaksmith: Deep in a cave, but I'm not sure exactly where.")

			if Op1==3:
				print("Blacksmith: Generally people rebut free will with determinism.")
				print("Blacksmith: But the argument is flawed.")
				print("Blacksmith: Determinism meerly means that you would re-do the same decisions.")

				O1="Well at this point the debate is meerly about definitions."
				O2="You never awnsered the question directly though."
				O3="Dude... You're tripping."
				Op2=self.ask([O1,O2,O3])

				if Op2==1:
					print("Blacksmith: I suppose.")
					print("Blacksmith: Though some definitions are better than others.")
					O1="How would you define free will?"
					O2="Neat."
					Op3=self.ask([O1,O2])

					if Op3==1:
						print("Blacksmith: The ability to chose an option based off surroundings.")
						print("Blacksmith: I guess the question now is what will you chose.")

				if Op2==2:
					print("Blacksmith: I will awnser with a question.")
					print("Blacksmith: Do you have free will now?")
					O1="Yes"
					Op3=self.ask([O1])

		if self.name=="Worker":
			if self.stage ==1:
				self.stage=2
				print("Worker: Yikes! A foreiner!.")
				print("Worker: What are you here for?")
			if self.stage ==2 or self.stage ==3:
				print("Worker: What do you want?")

			O1="What is life in the goblin village like?"
			O2="Are you discriminating against me since I'm a foreiner?"
			Op1=self.ask([O1,O2])

			if Op1==1:
				print("Worker:It's pretty rough.")
				print("Worker:The goblin king is working us too hard.")
				print("Worker:We can't follow our passions.")

				O1="What's your passion?"
				O2="How many people live around here?"
				O3="Sucks to suck!"
				Op2=self.ask([O1,O2,O3])

				if Op2==1:
					print("Worker: Mathmatics!")

					O1="YoUr a MatHmAtiCiaN? WhAt's 548x1809?"
					O2="What's 1+2+3+4+5..."
					O3="NERD."
					Op3=self.ask([O1,O2,O3])

					if Op3==1:
						print("Worker: Goddamit.")

					if Op3==2:
						print("Worker: -1/12, of course.")

						O1= "Who are you, Ramujan?"
						O2= "Um... divergence much?"
						O3= "This is why noone likes maths."
						Op4=self.ask([O1,O2,O3])

				if Op2==2:
					print("Worker:Too many.")
					print("Worker:We could make a bigger camp if the Goblin King would let us...")

			if Op1==2:
				print("Worker:No.")
				print("Worker:I was just pointing it out.")

				O1="Then why did you say 'Yikes' then?"
				O2="I guess I should check my privialge."
				Op2=self.ask([O1,O2])

				if Op2==1:
					print("Worker:I just did, OK?")
					print("Worker:Just drop it.")

					O1="Yeesh, no need to be touchy."
					O2="Im sorry, I didn't mean anything of it."
					O3="Lol."
					Op3=self.ask([O1,O2,O3])

					if Op3==2:
						print("Worker:It's all good.")



	def Attack(self,P):
		print(self.name + " dealt you "+str(int(self.dmg/Item(P.armor).arm))+" damage.")
		P.hp-=int(self.dmg/Item(P.armor).arm)
		if P.hp<=0:
			print(self.name +" has killed you!\n")
			P.die()