def magicSquare(n):
    magicsquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicsquare.append(l)
    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if (i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(i<0):
                i=n-1
            if(j==n):
                j=0
        if(magicsquare[i][j]!=0):
            i=i+1
            j=j-2
            continue
        else:
            magicsquare[i][j]=count
            count+=1
        i=i-1
        j=j+1
    for i in range(n):
        for j in range(n):
            print(magicsquare[i][j],end=" ");
        print()
def getValue():
    n=int(input("Value: "))
    if (n%2!=0):
        magicSquare(n)
    else:
        print("give odd numbers bitch!")
        print("do you want to continue the enter:1")
        l=int(input())
        if l==1:
            getValue()
        else:
            exit()
getValue()

        
