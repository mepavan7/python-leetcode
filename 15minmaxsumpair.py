def min_pair_sum(nums):
    nums.sort()
    max_sum = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        pair_sum = nums[l] + nums[r]
        max_sum = max(max_sum, pair_sum)
        l += 1
        r -= 1
    return max_sum
print(min_pair_sum([3, 5, 2, 3]))
print(min_pair_sum([3,5,4,2,4,6]))
        