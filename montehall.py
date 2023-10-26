import random 
doors=[0]*3
goat_door=[0]*2
swap=0
d_swap=0
j=0
while(j<10):
    x=random.randint(0,2)
    doors[x]='bmw'
    for i in range(0,3):
        if(i==x):
            continue
        else:
            doors[i]='goat'
            goat_door.append(i)
    choice=int(input("enter ur choice!"))
    door_open=random.choice(goat_door) 
    while(door_open==choice):
        door_open=random.choice(goat_door)
    print(door_open)
    print(doors)
    ch=input("Swap ?Y/N")
    if (ch=='y'):
        if(doors[choice]=='goat'):
            print("jeeta tunai")
            swap+=1
        else:
            print("haara tunai")
            swap=0
    else:
        if(doors[choice]=='goat'):
            print("haara tunai")
            d_swap=0
        else:
            print("jeeta tunai")
            d_swap+=1
    j+=1
            
            
                   
