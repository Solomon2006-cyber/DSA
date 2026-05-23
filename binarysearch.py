def binarysearch(a,key):
    low=0
    high=len(a)-1
    while low<=high:
        mid=(low+high)//2
        if key==a[mid]:
            return mid
        elif key>a[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1

a=[10,20,30,40,50,60,70,80]
key=int(input("Enter key value:"))
res=binarysearch(a,key)

if res==-1:
    print("Key not found")
else:
    print("Key found at index:",res)


    
    
