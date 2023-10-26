def binar_search(a,x):
    fisrt_pos=0
    last_pos=len(a)-1
    flag=0
    count=0
    while(fisrt_pos<=last_pos and flag==0):
        mid=(fisrt_pos+last_pos)//2
        if(x==a[mid]):
            print("element found at: ",(mid+1))
            flag=1
        elif(x<a[mid]):
            last_pos=mid-1
        elif(x>a[mid]):
            fisrt_pos=mid+1
        count+=1
    print("number of iteration: ",count)
def Linear_Search(a,x):
    count=0
    for i in a:
        if(x==a[i]):
            print("element found at ",i+1)
            break
        count+=1
    print("number of iteration: ",count)
a=[]
for i in range(1,1001):
    a.append(i)
x=100
print("***********BINARY")
binar_search(a,x)
print("***********Linear")
Linear_Search(a,x)


        
