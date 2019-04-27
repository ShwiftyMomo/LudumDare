class Board:
    def __init__(self):
        self.enemies=[]

    def turn(self,P):
        move=input()
        print("\n")

        if move == "help":
            I="(h)elp: see all possible actions \n"
            I+="(l)ocation: see current location \n"
            I+="(i)nfo: see all your stats \n"
            I+="e(x)amine + item: examine an item you possess \n"
            I+="(q)uit: leave the game \n"
            print(I)

        if move == "location" or move == "l":
            print(P.pos +"\n")

        if move == "info" or move == "i":
            print(P)

        if move.split(" ")[0] == "examine" or move.split(" ")[0] == "x":
            Str=""

            for i in move.split(" ")[1:]:
                Str+=i+" "

            Str=Str[:-1]

            item=P.items[[item.name for item in P.items].index(Str)]

            print(item)

        if move == "quit" or move == "q":
            print("Thanks for having played my game!")
            exit()