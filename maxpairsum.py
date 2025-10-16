def maxPairSum(nums, k):
    nums.sort()
    l = 0
    r = len(nums) - 1
    max_pair = -1
    while l < r:
        s = nums[l] + nums[r]
        if s < k:
            max_pair = max(max_pair, s)
            l += 1
        else:
            r -= 1
    return max_pair
# --- Testing the corrected function ---
# Correctly returns 58
print(maxPairSum([34, 23, 1, 24, 75, 33, 54, 8], 60))
# Correctly returns -1 (no sum is less than -10)
print(maxPairSum([1, 2, 3], -10))



import math

def maxPairSum(nums, k):
    nums.sort()
    l = 0
    r = len(nums) - 1
    
    # Initialize to negative infinity to correctly handle negative sums.
    max_sum = -math.inf 
    
    while l < r:
        s = nums[l] + nums[r]
        if s < k:
            max_sum = max(max_sum, s)
            l += 1
        else:
            r -= 1
            
    # If max_sum was never updated, no valid pair was found. Return -1.
    # Otherwise, return the closest sum we found.
    return -1 if max_sum == -math.inf else int(max_sum)

# --- Testing the new, correct function ---
print(f"Input: [-10, -5, -1], k = 0 -> Output: {maxPairSum([-10, -5, -1], 0)}")
print(maxPairSum([1, 2, 3], -10))