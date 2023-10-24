
month=['jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'august', 'sept', 'oct', 'nov', 'dec']
x=1

while(x<=12):
    if(x==2):
        print('we got 29 days in normal year and 28 days in leap year: ',month[x-1])
    elif(x%2==0 and x<7):
        print('we got 30 days',month[x-1])
    elif(x%2==0 and x>7):
        print('we got 31 days',month[x-1])
    elif(x%2!=0 and x<=7):
        print('we got 31 days',month[x-1])
    elif(x%2!=0 and x>7):
        print('we got 30 days',month[x-1])
    x+=1
