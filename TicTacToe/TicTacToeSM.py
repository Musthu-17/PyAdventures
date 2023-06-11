#Self_made
#Bugs_fixed:6
#Updates:3
import random


#Creation of set consisiting of elements x and o
board=[" " for x in range(9)]
#list for not repeating elements
num_used=[]
#The display of game
def The_gamebox():
   for row in [board[i*3:(i+1)*3]for i in range(3)]:
       print("| "+" | ".join(row)+" |")
#The sample display of game
def sample_gamebox():
    sample_board=[[str(i) for i in range(j*3,(j+1)*3)]for j in range(3)]
    for row in sample_board:
        print("| "+" | ".join(row)+" |")    
#playing the game
def players(ply,x_o):
       chosen_box=int(input("\nTurn for "+ply+": "))
       #for not repeating elements and choosing box
       while chosen_box in num_used or chosen_box>8:
            print("\nYou can't do that")
            chosen_box=int(input("\nTurn for "+ply+": "))            
       board[chosen_box]=x_o       
       num_used.append(chosen_box)   

def com():
    box_list=[1,2,3,4,5,6,7,8]
    chosen_box=random.choice(box_list)
    while chosen_box in num_used:
        chosen_box=random.choice(box_list)
    board[chosen_box]="X"
    num_used.append(chosen_box)
    

def plyr():
    chosen_box=int(input("\nYour turn"))
       #for not repeating elements and choosing box
    while chosen_box in num_used or chosen_box>8:
            print("\nYou can't do that")
            chosen_box=int(input("\nYour turn"))            
    board[chosen_box]="O"       
    num_used.append(chosen_box)
      

#The winning methods
def winner():
    global win
    for i in range(0,7,3):
        if board[i]==board[i+1]==board[i+2]!=" ":
            win=True
            
    if board[0]==board[4]==board[8]!=" ":
        win=True
       
    if board[2]==board[4]==board[6]!=" ":
        win=True
       
    for i in range(2):    
        if board[i]==board[i+3]==board[i+6]!=" ":
           win=True 
        




#to start loop         
win=False


def the_game():
    #in order to switch between players
    condition=True
 
#conditions to end game are no space left and winning
 
    while " " in board and win!=True:
        sample_gamebox()
        print("\n")
        The_gamebox()
        print("\n")
        
        if condition==True:
           players("Player1","X")
           condition=False
        else:
            players("Player2","O")
            condition=True
    
        winner()
          
   
    if " " in board:
        if condition==False:
            The_gamebox()
            print("Congrats,Player1 won the game")
        elif condition==True:
            The_gamebox()
            print("Congrats,Player2 won the game")
    else:
        The_gamebox()
        print("This game is a tie")          
   
    
def playervcom():
    
    #in order to switch between players
    condition=True

    
    while " " in board and win!=True:
        sample_gamebox()
        print("\n")
        The_gamebox()
        print("\n")
        if condition==True:
           plyr()
           condition=False 
        if condition==False:   
          com()
          condition=True
        winner()  
   
   
   
    
    if " " in board:
        if condition==False:
             The_gamebox()
             print("Congrats,you won the game")
        elif condition==True:
             The_gamebox()
             print("you lost the game")    
    else:
         The_gamebox()
         print("This game is a tie")   

def finale():
    print("1.PVP\n2.VsCOM")
    mode=input("Select mode: ")
    if mode==1:
        the_game()
    elif mode==2:
        playervcom()
    else:
        try:
            print("TRY AGAIN")
            ValueError()           
        except:
            pass 

finale()                  
