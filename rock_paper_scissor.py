user1=input("Name of player 1: ")
user2=input("Name of player 2: ")
user1_answer=input("Do you want to choose rock,paper or scissor?")
user2_answer=input("Do you want to choose rock,paper or scissor?")
def compare(u1,u2):
    if u1==u2:
        return "Its a tie!"
    elif u1=="rock":
        if u2=="scissor":
            return "Rock wins!"
        else:
            return "paper wins!"
    elif u1=="scissor":
        if u2=="paper":
            return "scissor wins!"
        else:
            return "rock wins!"
    elif u1=="paper":
        if u2=="rock":
            return "paper wins!"

        else:
            return "scissor wins!"
    else:
        return "Invalid input, try again!"
print(compare(user1_answer,user2_answer))
