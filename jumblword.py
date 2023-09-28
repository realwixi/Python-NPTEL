import random
def choose():
    words=['rainbow','star','love','suicide','assasination','words','cow','bitch']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled

def thank(name1,name2,p1,p2):
    print(name1 ," your points", p1)
    print(name2, " your points", p2)
    
    

def play():
    p1name=input("player1, please enter your name ")
    p2name=input("player2, please enter your name ")
    pp1=0
    pp2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print("the question is : ",qn)
        if turn%2==0:
            print(p1name," your turn")
            ans=input("whats on your mind?")
            if ans==picked_word:
                pp1=pp1+1
                print("Your score is: ",pp1)
            else:
                print("better luck next time")
        else:
            print(p2name," your turn")
            ans=input("whats on your mind?")
            if ans==picked_word:
                pp2=pp2+1
                print("Your score is: ",pp2)
            else:
                print("better luck next time")
        turn=turn+1
        c=int(input("press 1 to continue and 0 to quit"))
        if c==0:
            thank(p1name,p2name,pp1,pp2)
            break
play()
            
