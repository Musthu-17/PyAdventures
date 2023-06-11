import random 

def guess(x):
    random_number=random.randint(1,x)
    #print(f"Guess a number between 1 and {x}")
    a=0
    global n
    global j
    global k
    global l
    n=0 
    j="n"
    k="n"
    l="n"
    while a!=random_number:
       a=int(input())
       if a>random_number:
        #print("Sorry,You got it wrong.  Too high")
        j="y"
       elif a<random_number:
        #print("Sorry,You got it wrong.  Too low")
        k="y"
       elif a=="":
        #print("Type something dude") 
        l="y"
       n+=1 

    #print("congrats,You got it right")


guess(10)


def computer_guess(y):
    print(f"Pick a number between 1 and {y}")
    low=1
    high=y
    reply=''
    global m
    m=0
    while reply!='c':
        if low!=high:
            c_guess=random.randint(low,high)
        else:
            c_guess=low    
        reply=str(input(f"Is {c_guess} lower(L),Higher(H) or correct(C)").lower())
        if reply=="l":
            low=c_guess + 1
        elif reply=="h":
            high=c_guess - 1
        m+=1    
    print('Yay,I guessed correctly')        


computer_guess(10)

if n<m:
    print(f"its {n} to {m},you won")
elif n>m:
    print(f"its {n} to {m},you lost")
else:
    print(f'its {n} to {m},its a draw')    

