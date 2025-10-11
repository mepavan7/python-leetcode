def twosumlessthank(A, k):
    A.sort()
    l, r = 0, len(A)-1
    best = -1
    while l < r:
        s = A[l] + A[r]
        if s < k:
            best = max(best, s)
            l += 1
           
        else:
            r -= 1   
    return best
    
#print(twosumlessthank([34, 23, 1, 24, 75, 33, 54, 8], 60))
print(twosumlessthank([10, 20, 30], 15))
         
        