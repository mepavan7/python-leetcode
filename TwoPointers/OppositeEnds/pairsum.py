def twosum(nums, target):
    nums.sort()
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            return "Yes" 
        elif nums[l]+nums[r] < target:
            l += 1
        else:
            r -= 1
    return "No"
print(twosum([1,4,45,6,10,-8], 16))
print(twosum([1,4,45,6,10,-8], 27))