import random
year=random.randint(1900,2023) # you can also take the input
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("leap year")
else:
    print("not a leap Year")
