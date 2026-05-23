def selectionsort(a,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]>a[min]:
                min=j
                a[i],a[min]=a[min],a[i]
    return a

a=[14,21,27,41,43,45,46,57,70]
n=len(a)
print("List after sorting")
print(selectionsort(a,n))
 