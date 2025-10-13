def threesumsmaller(nums, target):  
    nums.sort()
    count = 0
    for i in range(len(nums)-2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            threesum = nums[i] + nums[l] + nums[r]
            if threesum < target:
                count += r - l
                l += 1
            else:
                r -= 1
        return count 
print(threesumsmaller([-2, 0, 1, 3], 2))

# Corrected Code
def threesumsmaller(nums, target):
    nums.sort()
    count = 0
    # The range can be optimized slightly to len(nums) - 2
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            threesum = nums[i] + nums[l] + nums[r]
            if threesum < target:
                # This part is perfect!
                count += r - l
                l += 1
            else: # Simplified from elif
                r -= 1
    return count
                
                
        