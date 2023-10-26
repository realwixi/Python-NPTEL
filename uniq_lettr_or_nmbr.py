def uniQ(s):
    cn={}
    for i in s:
        if i in cn:
            cn[i]+=1
        else:
            cn[i]=1
    uniq=[i for i, count in cn.items() if count==1]
    return uniq
def letters(x):
    new_letters={}
    for char in x:
        if char in new_letters:
            new_letters[char]+=1
        else:
            new_letters[char]=1
    return new_letters

print("**Important**")
x=input("do u want to enter a letter or number? type y for letter or type n for number: ")
if x=="Y" or x=='y':
    usr=str(input("Enter a letter: "))
    d=letters(usr)
    print(d)
elif x=='N' or x=="n":
    s=[int(i) for i in input("Enter a number: ")]
    print(uniQ(s))
    
    
