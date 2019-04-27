class Board:
    def __init__(self):
        self.enemies=[]

    def turn(self,P):
        move=input()
        print("\n")

        if move == "help":
            I="help: see all possible actions \n"
            I+="location: see current location \n"
            I+="info: see all your stats \n"
            I+="examine + item: examine an item you possess \n"
            print(I)

        if move == "location":
            print(P.pos +"\n")

        if move == "info":
            print(P)

        if move.split(" ")[0] == "examine":
            Str=""
            for i in move.split(" ")[1:]:
                Str+=i

            item=P.items[[item.name for item in P.items].index(Str)]

            print(item)

        if move == "exit":
            print("Thanks for playing my game!")
            Running=False