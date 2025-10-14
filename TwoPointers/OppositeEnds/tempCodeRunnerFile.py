def countPairs(nums, target):
    nums.sort()
    l, r = 0, len(nums) - 1
    count = 0
    while l < r:
        s = nums[l] + nums[r]
        if s < target:
            count += (r - 1)
            l += 1
        else:
            r -= 1
    return count
print(countPairs([-1,1,2,3,1], 2))
print(countPairs([-6,2,5,-2,-7,-1,3], -2))