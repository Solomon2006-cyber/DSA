def linearsearch(a,key,n):
    for i in range(0,n):
        if(a[i]==key):
            return i
    return -1


a=[10,20,30,40,50,60]
n=len(a)
key=int(input("Enter a number:"))
result=linearsearch(a,key,n)
if(result==-1):
    print("Element not found")
else:
    print("Element found at index:",result)
