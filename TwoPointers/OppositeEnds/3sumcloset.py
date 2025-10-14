import math
def three_Sum_Closest(nums, target):
    min_dff = math.inf
    closest_sum = 0
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                curr_sum = nums[i] + nums[j] + nums[k]
                curr_diff = abs(curr_sum - target)
                if curr_diff < min_dff:
                    min_dff = curr_diff
                    closest_sum = curr_sum
    return closest_sum
print(three_Sum_Closest([-1,2,1,-4], 1))
    
#Opposite End   
import math
def three_Sum_Closest(ar, t):
    min_diff = math.inf
    closest_sum = 0
    ar.sort()
    for i in range(len(ar)):
         # --- OPTIMIZATION ADDED HERE ---
        # If the current number is the same as the one before it, skip it.
        if i > 0 and ar[i] == ar[i-1]:
            continue
        l, r = i+1, len(ar) - 1
        while l < r:
              curr_sum =  ar[i] + ar[l] + ar[r]
              curr_diff = abs(curr_sum - t)
              if curr_diff < min_diff:
                 min_diff = curr_diff
                 closest_sum = curr_sum
            
              if curr_sum < t:
                 l += 1
              else:
                r -= 1
    return closest_sum
print(three_Sum_Closest([-1,2,1,-4], 1))
print(three_Sum_Closest([1, 1, 1, 0], 100))      
print(three_Sum_Closest([-4, -1, 1, 2], 1))      
        
         
                
            
            