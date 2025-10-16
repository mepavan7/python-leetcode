def counttriplet(nums, k):
    nums.sort()
    count = 0
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i]+nums[l]+nums[r]
            if s < k:
                count += r - l
                l += 1
            else:
                r -= 1
    return count
print(counttriplet([-2, 0, 1, 3], 2))
print(counttriplet([5, 1, 3, 4, 7], 12))
        
        