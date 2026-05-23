def bubblesort(a,n):
    for i in range(n):
        for j in range(n-i-1):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=["C","S","I","P","L","E","A","R","N","I","N","G"]
n=len(a)
print("list after sorting")
print(bubblesort(a,n))

