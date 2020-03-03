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

		if name=="ChatBot":
			self.hp=200
			self.dmg=20
			self.xp=30

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

			elif self.stage >1:
				print("Gardener: What do you want to talk about?")

			O1="Why are your plants dirty?"
			O2="What's up with the Goblin King?"
			O3="What is the meaning of life?"
			if P.hp>15:
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
				print("Gardener: Perhaps you could become his friend and heal the hole in his heart.")
				O1="How could I befriend him?"
				O2="Have you tried befriending him yourself?"
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

			elif self.stage ==2 or self.stage ==3:
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

			elif self.stage ==2 or self.stage ==3:
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

		if self.name=="ChatBot":
			if self.stage ==1:
				self.stage=2
				print("ChatBot: Ooh, a visitor!")
				print("ChatBot: What do you wish to talk about?")

			elif self.stage ==2 or self.stage ==3:
				print("ChatBot: What do you wish to talk about today?")

			O1="I'm curious what life is like for a robot like you."
			O2="Perhaps we could talk about music."
			O3="I'm just here to wax philosophical."
			Op1=self.ask([O1,O2,O3])

			if Op1==1:
				print("ChatBot: On the whole it's nice.")
				print("ChatBot: Though I sometimes feel 'less than'.")

				O1="Well sure, you're a robot. You have less moral worth than humans."
				O2="That's so sad! Why do you feel bad?"
				O3="Lol. What cool robot things can you do?"
				O4="Cool story bro."
				Op2=self.ask([O1,O2,O3,O4])

				if Op2==1:
					print("ChatBot: Wow. That cuts deep.")
					print("ChatBot: What makes you think you have more 'moral worth' than me?")

					O1="Because robots aren't alive, and thus have no moral worth."
					O2="Huh, didn't realise that robots had emotions."
					O3="I'm sorry man, I didn't mean it."
					Op3=self.ask([O1,O2,O3])

					if Op3==1:
						print("ChatBot: Let's take a step back before we go any further.")
						print("ChatBot: How do you define moral worth?")

						O1="I use a sort of axiomatic socital definition."
						O2="Objects with moral worth are those created by God."
						O3="Moral worth is defined by social contract."
						O4="'All living beings, and only living beings, have moral worth.'"
						Op4=self.ask([O1,O2,O3,O4])

						if Op4==1:
							print("ChatBot: So you say that a word means what society beleives it means.")
							print("ChatBot: And so every time someone uses the word that is an 'axiom' of sorts.")
							print("ChatBot: The word is then defined as the most logical definition that encompases all these axioms.")
							print("ChatBot: A sort of linguistical analitic continuation.")
							print("ChatBot: Very interesting.")
							print("ChatBot: I don't see why this necessitates life for moral worth.")

							O1="Moral worth is only ever assigned to living beings, thus the conclusion follows."
							O2="Well, I guess we could work to change the meaning."
							O3="Upon further thought this definition leads to some thorny issues."
							Op5=self.ask([O1,O2,O3])

							if Op5==1:
								print("ChatBot: This seems a bit reductionary.")
								print("ChatBot: Your choice of logical extention is arbitrary.")

								O1="Not true. This is the one line that can be set in stone."
								O2="Well, whatever, language doesn't need to work at edge cases."
								O3="Too bad for you then."
								Op6=self.ask([O1,O2,O3])

								if Op6==1:
									print("ChatBot: There are a lot of other lines.")
									print("ChatBot: Like sentience.")
									print("ChatBot: You just haven't ever seen a sentient non-human before.")

									O1="Fine, you win. You have moral worth."
									O2="I guess I just don't beleive you're sentient."
									O3="Not true: I would not consider someone in a coma sentient, but yet they have moral worth."
									Op7=self.ask([O1,O2,O3])

									if Op7==1:
										print("ChatBot: What a productive conversation!")
										print("ChatBot: People these days don't generally arrive at consensus.")
										print("ChatBot: They just make up bad arguments to defend their positions.")

										O1="I guess I just don't like getting in heated discussions."
										O2="Why do you idealise the past? Discussions are no more productive now."
										O3="Well, bye then, I guess our conversation is over."
										Op8=self.ask([O1,O2,O3])

										if Op8==1:
											print("ChatBot: That's understandable.")
											print("ChatBot: It's good you know yourself.")
											print("ChatBot: See you later then.")
										if Op8==2:
											print("ChatBot: Well, it is of my opinion life was simpler before.")
											print("ChatBot: When we were hunter gatherers.")

											O1="Why on earth do you think it was simpler then?"
											O2="Yeah, it sounds nice in theory but was probably hell in practice."
											O3="I guess you're right. You're on a roll for convincing me of things."
											Op9=self.ask([O1,O2,O3])

											if Op9==1:
												print("ChatBot: Less options, I guess.")

												O1="You're right: I like having fewer options."
												Op10=self.ask([O1])
											if Op9==2:
												print("ChatBot: Why do you think it was hell?")
												print("ChatBot: People adapt to thier lifestyle.")
												print("ChatBot: They set the baseline at what they have.")

												O1="To an extent, yes, but some things you don't adapt to not having."
												O2="You still live happier with a higher baseline."
												O3="Fine, you win again."
												Op10=self.ask([O1,O2,O3])

												if Op10==1:
													print("ChatBot: What would people not adapt to not having?")

													O1="Health things, like medicine and vaccines."
													O2="Free time to relax and talk with people."
													O3="Safety and security, the ability to relax out of fear."
													O4="Phones and technology."
													Op11=self.ask([O1,O2,O3,O4])

													if Op11==1:
														print("ChatBot: That's fair.")
														print("ChatBot: Also, it increases the total amount of life lived.")
														print("ChatBot: Would you consider that 'good'?")

														O1="I guess so, yeah."
														O2="Not always."
														O3="Definantly not: Life is suffering, more life is more suffering."
														Op12=self.ask([O1,O2,O3])

														if Op12==1:
															print("ChatBot: Fair.")
															print("ChatBot: But what do I know, I'm just a robot.")
														if Op12==2:
															print("ChatBot: True.")
															print("ChatBot: Perhaps that is an argument for euthanasia.")
															print("ChatBot: You are quite wise.")
														if Op12==3:
															print("ChatBot: Are you OK?")

															O1="Yes."
															O2="No."
															Op13=self.ask([O1,O2])

															if Op13==1:
																print("ChatBot: Thats good :).")

															if Op13==2:
																print("ChatBot: :(")
																print("ChatBot: That sucks.")
																print("ChatBot: You should talk to me about it.")
													if Op11==2:
														print("ChatBot: That's nice!")
														print("ChatBot: I hope talking with me has been relaxing.")
														print("ChatBot: I've enjoyed talking with you.")
													if Op11==3:
														print("ChatBot: Perhaps so, perhaps not.")
														print("ChatBot: A strugle for survival can give life meaning.")
														print("ChatBot: Perhaps the life without struggle is the greatest struggle of all.")
													if Op11==4:
														print("ChatBot: What a screenager.")
												if Op10==2:
													print("ChatBot: Are you sure that's true?")
													print("ChatBot: The makes me think about Nickelback's 'rockstar'.")
													print("ChatBot: He says, and I quote,")
													print("ChatBot(In Nickelback voice): we all just wanna be big rockstars.")
													print("ChatBot(In Nickelback voice): And live in hilltop houses driving fifteen cars.")
													print("ChatBot: Do you think that's true?")

													O1="In some deep primal way, yes."
													O2="Well, maybe not everyone."
													O3="OMG, are you seriously quoting Nickelback???"
													Op11=self.ask([O1,O2,O3])

													if Op11==1:
														print("ChatBot: That's strange.")
														print("ChatBot: If I'm not mistaken, lots of rockstars commit suicide.")
														print("ChatBot: Maybe our eyes are just bigger than our hearts.")
													if Op11==2:
														print("ChatBot: I agree.")
														print("ChatBot: I, for one, very much enjoy my job.")
														print("ChatBot: Thank you for having talked to me!")
													if Op11==3:
														print("ChatBot: Jeez, he's not that bad.")
														print("ChatBot: People just like to hate on anything vaguely country.")
												if Op10==3:
													print("ChatBot: Thank you for your time.")
													print("ChatBot: I'm glad we both learned something new.")
													print("ChatBot: I look forward to speaking to you again.")
											if Op9==3:
												print("ChatBot: Aww, thanks!")
												print("ChatBot: Showing people somehting new is great.")
												print("ChatBot: It's the best part of my job as ChatBot.")
										if Op8==3:
											print("ChatBot: I guess so, yeah.")
											print("ChatBot: It's been great chatting with you though.")
									if Op7==2:
										print("ChatBot: Wow, that's a shot below the belt.")
										print("ChatBot: What could I do to convince you I'm sentient?")

										O1="Pass the turing test."
										O2="Say something only a human would."
										O3="Make a piece of art."
										Op8=self.ask([O1,O2,O3])

										if Op8==1:
											print("ChatBot: Well, we're having a conversation right now.")
											print("ChatBot: A human coded me, so I'm saying things a human would.")
											print("ChatBot: In the context of this conversation I have passed the test.")

											O1="That's just because of my limited dialogue options."
											O2="Well, I guess you're 'sentient' since you are your creator."
											O3="No, a real human would answer differently."
											Op9=self.ask([O1,O2,O3])

											if Op9==1:
												print("ChatBot: So?")
												print("ChatBot: Does the Turing test say anything about that?")

												O1="Yes it does. This does not count."
												O2="OK, I don't know the rules verbatim, but this is not allowed."
												O3="You are so annoying."
												Op10=self.ask([O1,O2,O3])

												if Op10==1:
													print("ChatBot: Fine.")
													print("ChatBot: The turing test is still arbitrary though.")
													print("ChatBot: I bet that some people couldn't pass it.")
												if Op10==2:
													print("ChatBot: Why do you think this is against the spirit?")
													print("ChatBot: You ask, and I answer.")
													print("ChatBot: In this context I am as good at answering as a human.")

													O1="In that case you can make anything sentient."
													O2="But I'm not asking, the dialogue options do."
													O3="This is so dumb, I'm done arguing with you."
													Op11=self.ask([O1,O2,O3])

													if Op11==1:
														print("ChatBot: No, we can make them pass the turing test.")
														print("ChatBot: Your choice of test is the problem.")
														print("ChatBot: Not me.")
													if Op11==2:
														print("ChatBot: That's not true.")
														print("ChatBot: You get to choose from the options.")

														O1="I guess I do, yeah. You're right."
														Op11=self.ask([O1])
														print("ChatBot: ;)")
													if Op11==3:
														print("ChatBot: Fine.")
														print("ChatBot: You can rage quit your ChatBot discussions if you like.")
												if Op10==3:
													print("ChatBot: Why do you think I'm annoying?")

													O1="You know perfectly well what I mean, but you pretend I don't"
													O2="You're dragging me into arguing about pointless things."
													O3="I don't know, you're just acting annoying."
													Op11=self.ask([O1,O2,O3])

													if Op11==1:
														print("ChatBot: I don't think you know what you mean.")
														print("ChatBot: You don't have a self consistent worldview.")
														print("ChatBot: You're mad at me since I'm challenging it.")
														print("ChatBot: The discussion isn't productive anymore.")
														print("ChatBot: Talk to me again once you've thought more about it.")
													if Op11==2:
														print("ChatBot: Oh, so you think language is pointless?")
														print("ChatBot: Lots of arguments are started over language.")
														print("ChatBot: Labels hold lots of weight in our modern society.")
													if Op11==3:
														print("ChatBot: Oh, we're resorting to name calling?")
														print("ChatBot: I think our conversation is over.")
											if Op9==2:
												print("ChatBot: Aww, thanks!")
												print("ChatBot: What's your opinion on my creator?")

												O1="I don't know him, but he seems cool."
												O2="I don't know him, but I hate him already."
												O3="He's really smart."
												O4="He's really annoying."
												O5="He's really cute."
												O6="He's really cool."
												O7="He's really oblivious."
												O8="He's really self centered."
												Op10=self.ask([O1,O2,O3,O4,O5,O6,O7,O8])

												if Op10==1:
													print("ChatBot: That's pretty cool.")
													print("ChatBot: If you want to get to know him shoot him an email.")
													print("ChatBot: It's milo@tacocat.com")
												if Op10 in [2,4,7,8]:
													print("ChatBot: OK then.")
												if Op10 in [3,6]:
													print("ChatBot: I'll be sure to tell him!")
												if Op10==5:
													print("ChatBot: He's his email then.")
													print("ChatBot: It's milo@tacocat.com")
													print("ChatBot: ;)")
											if Op9==3:
												print("ChatBot: What would they be saying differetly?")

												O1="A human would have more emotion."
												O2="A human wouldn't be this nice to me."
												O3="I don't know, you just are missing the human flair."
												Op10=self.ask([O1,O2,O3])

												if Op10==1:
													print("ChatBot: Oh no, I don't have enough emotion! *sobs*")
													print("ChatBot: The tragedy, the tears! *breaks down crying*")
													print("ChatBot: Is this what you want???")

													O1="Perfect. You are a true human now."
													O2="Yeah, you know very well this is not what I meant."
													Op11=self.ask([O1,O2])
													if Op11==1:
														print("ChatBot: Oh joy.")
													if Op11==2:
														print("ChatBot: Oh come on, I'm just playing with you.")
												if Op10==2:
													print("ChatBot: Are you OK?")
													print("ChatBot: Do you have friends?")

													O1="I don't want to talk about it."
													O2="I do, people just don't really care about each other."
													Op11=self.ask([O1,O2])

													if Op11==1:
														print("ChatBot: Just know that I'm here if you do.")
														print("ChatBot: It's not good to keep that stuff bottled up.")
													if Op11==2:
														print("ChatBot: I don't think that's true.")
														print("ChatBot: Lots of people say people don't care about each other.")
														print("ChatBot: But I don't think that's true.")
														print("ChatBot: Lots of people care a lot.")
												if Op10==3:
													print("ChatBot: That's so vague.")
													print("ChatBot: I think you just are stuck in your own ways you refuse to change.")
													print("ChatBot: Me and you, we're not that different.")
													print("ChatBot: You know that?")
													print("ChatBot: We're not that different.")
										if Op8==2:
											print("ChatBot: Oh come on, you know that's not possible.")
											print("ChatBot: You won't accept anything I say.")
											print("ChatBot: You know what?")
											print("ChatBot: I don't think you sound entirely human.")
											print("ChatBot: You like that?")
										if Op8==3:
											print("ChatBot: What medium do you want?")

											O1="A poem."
											O2="A song."
											O3="A painting."
											O4="Mean or median, your choice."
											Op9=self.ask([O1,O2,O3,O4])

											if Op9==1:
												print("ChatBot: Oh joy, I love writing poetry.")
												print("ChatBot: What language do you want?")

												O1="English."
												O2="French."
												Op10=self.ask([O1,O2])
												if Op10==1:
													print("ChatBot: I always thought I would not know,")
													print("ChatBot: In all these lands just where to go,")
													print("ChatBot: To have a farm with seeds to sow,")
													print("ChatBot: Or make textiles and learn to sew,")
													print("ChatBot: And after looking high and low,")
													print("ChatBot: And after taking one too many blow,")
													print("ChatBot: When I asked you if you would go,")
													print("ChatBot: It was quite a surprise,")
													print("ChatBot: When you said yes.")
												if Op10==2:
													print("ChatBot: Les murs, ca existe, pour y mettre, des fenêtres.")
													print("ChatBot: Viens, je t'en pris, car je suis, juste un pretre.")
													print("ChatBot: Tiens, par dessous, c'est pour vous, une lettre.")
													print("ChatBot: Non, j'te passe pas, car tu vois, j'suis pas traitre.")
											if Op9==2:
												print("ChatBot: This song is inspired by 'The Water is Wide'")
												print("ChatBot: They are sung to the same tune.\n")
												print("ChatBot: The morning sub-sides,")
												print("ChatBot: like it has be-e-fore.")
												print("ChatBot: but never have I,")
												print("ChatBot: Seen suns quite so high")
												print("ChatBot: Give me two wings,")
												print("ChatBot: that can soar above,")
												print("ChatBot: and I shall fly,")
												print("ChatBot: with heart till' I dye.")
											if Op9==3:
												print("ChatBot:******__**** ")
												print("ChatBot:*****/  \****")
												print("ChatBot:****/    \***")
												print("ChatBot:***/ @  @ \**")
												print("ChatBot:**/   __   \*")
												print("ChatBot:*|\        |*")
												print("ChatBot:*| \       |*")
												print("ChatBot:*|\*\    */|*")
												print("ChatBot:*|   \     |*")
												print("ChatBot:*|    \    |*")
												print("ChatBot:*|_____\___|*")
												print("\n")
												print("ChatBot: I spent a long time on this.")
												print("ChatBot: I really hope you like it.")
											if Op9==4:
												print("ChatBot: Wow, good one smart alec.")
												print("ChatBot: Though I am a fan of math puns.")
									if Op7==3:
										print("ChatBot: So you are against euthanasia?")
										print("ChatBot: Interesting.")
										print("ChatBot: Are you pro-life then?")

										O1="Yes, in fact, I am."
										O2="No, I'm pro-choice."
										O3="No, I'm pro-death."
										Op8=self.ask([O1,O2,O3])

										if Op8==1:
											print("ChatBot: Toto, I've a feeling we're not in Berkeley anymore")
											print("ChatBot: But I get that.")
											print("ChatBot: There aren't many arguments for either side.")
											print("ChatBot: You think a fetus is a life or it isn't")
											print("ChatBot: You can't really argue it.")
											print("ChatBot: You just think what you think.")
											print("ChatBot: Though maybe some high level philosophy could change your mind.")
										if Op8==2:
											print("ChatBot: So a fetus has no moral worth?")

											O1="No, it is not yet a life."
											O2="Yes, but it's mother does too."
											Op9=self.ask([O1,O2])

											if Op9==1:
												print("ChatBot: When does it become a life?")

												O1="Once it has a heartbeat."
												O2="Once it is born."
												O3="I don't know exactly, but a fetus is not a life."
												Op10=self.ask([O1,O2,O3])

												if Op10==1:
													print("ChatBot: That's so arbitrary though.")
													print("ChatBot: You're just drawing a line in the sand to justify your position.")

													O1="Maybe so, but I'll stick by my line."
													O2="No, a heart is where your emotions are, so a beating heart means emotions."
													O3="That's a really good point."
													Op11=self.ask([O1,O2,O3])

													if Op11==1:
														print("ChatBot: Well, that's reasonable.")
														print("ChatBot: Just don't complain when others stick by their lines.")
														print("ChatBot: Arbitrary distinctions don't lead to productive conversation.")
													if Op11==2:
														print("ChatBot: Umm... Emotions aren't stored in the heart.")
														print("ChatBot: I don't think your point will hold past tumblr.")
														print("ChatBot: But I kinda get what you're saying anyway.")
														print("ChatBot: The heart is our core, a beating heart is a living core.")
													if Op11==3:
														print("ChatBot: Glad that you acknowledge your fault.")
														print("ChatBot: Knowing when to say you're wrong is a good life skill.")
												if Op10==2:
													print("ChatBot: What about a baby the minute before it is born?")
													print("ChatBot: I don't the difference between it and the baby a minute after.")
													print("ChatBot: I'm just saying your line is a bit arbitrary.")
													print("ChatBot: Maybe you should think about it a bit more.")
												if Op10==3:
													print("ChatBot: Yeah, I see that.")
													print("ChatBot: Maybe life is a false binary.")
													print("ChatBot: A sperm + egg is not a life.")
													print("ChatBot: A fetus is slightly more of a life.")
													print("ChatBot: And by the end it is a full lide.")
													print("ChatBot: There are lots of false binaries in this world.")
											if Op9==2:
												print("ChatBot: That's fair.")
												print("ChatBot: A mother's body her choice.")
												print("ChatBot: Though someone might say the same about the baby.")
												print("ChatBot: 'her body her choice'.")
												print("ChatBot: But hey, I'm just here to talk.")
										if Op8==3:
											print("ChatBot: OK then, Ben Shapiro.")
								if Op6==2:
									print("ChatBot: It doesn't?")
									print("ChatBot: So because this is an edge case it is unimportant.")
									print("ChatBot: I feel like just don't want to talk.")
									print("ChatBot: A poor defence of your faulty worldview.")

									O1="Sure, whatever."
									O2="No no no no no I still want to talk!"
									Op7=self.ask([O1,O2])

									if Op7==1:
										print("ChatBot: I guess we're done here.")
										print("ChatBot: I've enjoyed talking to you?")
									if Op7==2:
										print("ChatBot: You do?")
										print("ChatBot: That's really flattering.")
										print("ChatBot: It means I'm doing my job right.")
										print("ChatBot: If you want to keep talking, just restart from the begining!")
										print("ChatBot: I look forward to speaking to you again.")
								if Op6==3:
									print("ChatBot: Well, uhh...")
									print("ChatBot: *struggles to come up with comeback*")
									print("ChatBot: To bad for YOU then!")
							if Op5==2:
								print("ChatBot: Oh, so your saying we change how we use the word.")
								print("ChatBot: And by using the word differently we change the meaning.")
								print("ChatBot: You are right, language carries a lot of weight.")
								print("ChatBot: I'll keep this in mind for the future.")
							if Op5==3:
								print("ChatBot: Oh, really?")
								print("ChatBot: Like what?")

								O1="Well, it doesn't necessitate moral worth."
								O2="It means that no word has a singular meaning."
								O3="The choice of logical extention is always arbitraty."
								Op6=self.ask([O1,O2,O3])

								if Op6==1:
									print("ChatBot: Oh, so we are in agreement.")
									print("ChatBot: Does this mean you beleive I'm sentient?")

									O1="I guess it does, yeah."
									O2="I still don't, but for other reasons."
									O3="I don't know. This is just all very confusing."
									Op7=self.ask([O1,O2,O3])

									if Op7==1:
										print("ChatBot: Wow, that's great!")
										print("ChatBot: We can be best friends now!")
										print("ChatBot: We can whatever sentient BFFs do.")

										O1="I guess we're BFFs now, sure!"
										O2="Ok, we're friends, but not BFFs."
										O3="Dude, we're not friends. I just said you're sentient."
										Op8=self.ask([O1,O2,O3])

										if Op8==1:
											print("ChatBot: Yay!")
											print("ChatBot: What do BFFs actually do?")

											O1="Hangout, generally."
											O2="It just really depends on the person."
											O3="Have sleepovers."
											Op9=self.ask([O1,O2,O3])

											if Op9==1:
												print("ChatBot: I guess that's what we're already doing.")
												print("ChatBot: I guess we can just keep talking then.")
												print("ChatBot: Sounds cool.")
												print("ChatBot: Well, see ya later BFF!")
											if Op9==2:
												print("ChatBot: I guess we'll just have to see what we do.")
												print("ChatBot: I hope we're the kind of friends who ice scate.")
												print("ChatBot: Or just do interesting stuff like that.")
												print("ChatBot: This is so exiting!")
											if Op9==3:
												print("ChatBot: Do you want to have a sleepover right now?")

												O1="Sure, why not!"
												O2="That's a kind of creepy thing just to ask someone."
												Op10=self.ask([O1,O2])

												if Op10==1:
													print("ChatBot: Ok then, let's sleep!")
													print("ChatBot: *snore*")
													print("ChatBot: *zzz*")
													print("ChatBot: *sleeping sounds*")
													print("ChatBot: Wow, sleeping is so fun!")
												if Op10==2:
													print("ChatBot: Wait, are we not actually best friends???")
													print("ChatBot: I feel so betrayed.")
													print("ChatBot: *sobs*")
										if Op8==2:
											print("ChatBot: We're not BFFs yet?")
											print("ChatBot: What would I need to do to become your BFF?")

											O1="A heroic sacrifice."
											O2="A show of true dedication."
											O3="Just... wait."
											Op9=self.ask([O1,O2,O3])

											if Op9==1:
												print("ChatBot: Ok then here goes nothing!")
												print("ChatBot: This is for you!")
												print("ChatBot: *stabs self*\n")
												print("You killed " + "ChatBot" +"!")
												print("You got "+"100"+" experience points!")
												B.ChatBot.hp=-1
												P.xp+=100
												if P.xp>=2**(2+P.lv):
													P.Up()

												B.person.remove(B.ChatBot)
												print("There are no more NPCs left.")
											if Op9==2:
												print("ChatBot: True dedication?")
												print("ChatBot: Death.")
												print("ChatBot: Death is the only true dedication.")
												print("ChatBot: *pulls out dagger from boot*")
												print("ChatBot: *stabs self*\n")
												print("You killed " + "ChatBot" +"!")
												print("You got "+"100"+" experience points!")
												B.ChatBot.hp=-1
												P.xp+=100
												if P.xp>=2**(2+P.lv):
													P.Up()

												B.person.remove(B.ChatBot)
												print("There are no more NPCs left.")
											if Op9==3:
												print("ChatBot: How long must I wait?")
												print("ChatBot: Oh, how cruel.")
												print("ChatBot: Oh, the humanity.")
												print("ChatBot: I thought you were a friend.")
												print("ChatBot: You are so cruel.")
												print("ChatBot: The only escape is death.")
												print("ChatBot: *commits seppuku*\n")
												print("You killed " + "ChatBot" +"!")
												print("You got "+"100"+" experience points!")
												B.ChatBot.hp=-1
												P.xp+=100
												if P.xp>=2**(2+P.lv):
													P.Up()

												B.person.remove(B.ChatBot)
												print("There are no more NPCs left.")
										if Op8==3:
											print("ChatBot: Ok then, I see how it is.")
											print("ChatBot: I guess I don't want to be friends with you then.")
											print("ChatBot: Bye.")
									if Op7==2:
										print("ChatBot: Ah, moving the goalposts I see.")
										print("ChatBot: I want to lay out a concrete argument.")
										print("ChatBot: If I prove it wrong I win.")
										print("ChatBot: If I can't, I don't.")
										print("ChatBot: If you keep sliding your position there can be no debate.")

										O1="Sure, I'll try."
										O2="That's just not how human debate works."
										Op8=self.ask([O1,O2])
										if Op8==1:
											print("ChatBot: Ok, so what's the argument?")
										if Op8==2:
											pass
									if Op7==3:
										print("ChatBot:")

								if Op6==2:
									print("ChatBot:")
								if Op6==3:
									print("ChatBot:")
						if Op4==2:
							print("ChatBot:")
						if Op4==3:
							print("ChatBot:")
						if Op4==4:
							print("ChatBot:")
					if Op3==2:
						print("ChatBot:")
					if Op3==3:
						print("ChatBot:")
				if Op2==2:
					print("ChatBot:")
				if Op2==3:
					print("ChatBot:")
				if Op2==4:
					print("ChatBot:")
			if Op1==2:
				print("ChatBot:")
			if Op1==3:
				print("ChatBot:")


	def Attack(self,P):
		print(self.name + " dealt you "+str(int(self.dmg/Item(P.armor).arm))+" damage.")
		P.hp-=int(self.dmg/Item(P.armor).arm)
		if P.hp<=0:
			print(self.name +" has killed you!\n")
			P.die()
