import random

def playrps():

    user=input("Pick your choice: r for rock , p for paper , s for scissors s")
    com=random.choice(["r","p","s"])
     
    if user==com:
        return "It\'s a tie"
     
    if winning(user,com):
        return "you won"

    return "you lost"

def winning(player,opponent):
    if player=="r"  and opponent=="s" or player=="p" and opponent=="r" or player=="s" and opponent=="p":
        return True
    
   
print(playrps())    