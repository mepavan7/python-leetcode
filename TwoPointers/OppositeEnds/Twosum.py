def twosum(nums, target):
    l, r = 0, len(nums)-1
    while l < r:
        if nums[l] + nums[r] == target:
            return nums[l], nums[r]
        elif nums[l]+nums[r] < target:
            l += 1
        else:
            r -= 1
    return False
#test example
print(twosum([2,7,11,15], 9))
print(twosum([2,3,4], 6))
print(twosum([-1,0], -1))
