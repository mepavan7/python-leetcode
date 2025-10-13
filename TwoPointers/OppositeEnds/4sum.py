def four_sum(nums, target):
    li = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, len(nums)):
            if j > i + 1 and nums[j] == nums[j-1]:
                continue
            l = j + 1
            r = len(nums) - 1
            while l < r:
                foursum = nums[i] + nums[j] + nums[l] + nums[r]
                if foursum == target:
                    li.append([nums[i], nums[j], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                elif foursum < target:
                    l += 1
                else:
                    r -= 1
                   
    return li
print(four_sum([1, 0, -1, 0, -2, 2], 0))
print(four_sum([2,2,2,2,2], 8))
print(four_sum([-1,-5,-5,-3,2,5,0,4], -7))
                    
            