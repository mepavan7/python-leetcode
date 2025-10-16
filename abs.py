import math
def absolutedifference(nums,T):
    min_difference = math.inf
    close_sum = 0
    #res = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            curr_sum = nums[i] + nums[j]
            current_difference = abs(curr_sum - T)
           # res.append((current_difference))
            #res.append((curr_sum))
            if current_difference< min_difference:
                min_difference = current_difference
                close_sum = curr_sum
            
    return   close_sum
# Example usage:
nums = [10, 22, 28, 29, 30, 40]
target = 54
print(f"Brute-force result:{absolutedifference(nums,target)}")

#Oppsite Ends 
import math
def find_closet_sum(arr, T):
    arr.sort()
    n = len(arr)
    min_diff = math.inf
    best = -1
    l, r = 0, n - 1
    while l < r:
        curr_sum = arr[l] + arr[r]
        curr_diff = abs(curr_sum - T)
        if curr_diff < min_diff:
            min_diff = curr_diff
            best = curr_sum
        if curr_sum < T:
            l += 1
        else:
            r -= 1
    return best

# Example usage:
nums = [10, 22, 28, 29, 30, 40]
target = 54
print(f"Opposite End result:{find_closet_sum(nums,target)}")
        