def findclosestelememts(arr, k , x):
    arr.sort()
    l = 0
    r = len(arr)-1
    while r - l + 1 > k:
        if (x - arr[l] > arr[r] - x):
            l += 1
        else:
            r -= 1
    return arr[l:r+1]
print(findclosestelememts([1,2,3,4,5], 4, 3))