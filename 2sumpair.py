import math
def pair_sum_closest(arr, target):
    # 1. Handle the edge case where no pair can be formed.
    if len(arr) < 2:
        return []
    arr.sort()
    l = 0
    r = len(arr) - 1
    mindiff = math.inf
    resultantpair = []
    while l < r:
        currsum = arr[l] + arr[r]
        currdiff = abs(currsum - target)
        if currdiff < mindiff:
            mindiff = currdiff
            resultantpair = [arr[l], arr[r]]
         # 2. Check if we found a closer pair OR a tie-breaking pair.
        elif currdiff == mindiff:
            if abs(arr[l] - arr[r]) > abs(resultantpair[0] - resultantpair[1]):
                resultantpair = [arr[l], arr[r]]
        if currsum < target:
            l += 1
        else:
            r -= 1
    return resultantpair
# --- Testing the corrected function ---
print(f"Input: [10, 30, 20, 5], Target: 25 -> Output: {pair_sum_closest([10, 30, 20, 5], 25)}")
print(f"Input: [5, 2, 7, 1, 4], Target: 10 -> Output: {pair_sum_closest([5, 2, 7, 1, 4], 10)}")
print(f"Input: [10], Target: 10 -> Output: {pair_sum_closest([10], 10)}")
   
            
        
            
        
    
    