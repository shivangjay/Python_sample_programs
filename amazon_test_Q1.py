locations = [1,5,2,6]
movedf = [1,4,5,7]
movedto = [4,7,1,3]
#merge sort
MergeSort(A, p, r):
    if p > r 
        return
    q = (p+r)/2
    mergeSort(A, p, q)
    mergeSort(A, q+1, r)
    merge(A, p, q, r)
for i in range(len(locations)):
    for j in range(len(movedf)):
        if movedf[j] == locations[i]:
            locations[i] = movedto[j]
locations.MergeSort()
print(locations)
locations = [1,5,2,6]
movedf = [1,4,5,7]
movedto = [4,7,1,3]
for i in range(len(locations)):
    for j in range(len(movedf)):
        if movedf[j] == locations[i]:
            locations[i] = movedto[j]
locations.MergeSort()
print(locations)
locations = [1,5,2,6]
movedf = [1,4,5,7]
movedto = [4,7,1,3]
for i in range(len(locations)):
    for j in range(len(movedf)):
        if movedf[j] == locations[i]:
            locations[i] = movedto[j]
locations.MergeSort()
print(locations)
