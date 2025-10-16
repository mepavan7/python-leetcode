def count_pairs(nums, target):
    nums.sort()
    count = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        s = nums[l] + nums[r]
        if s < target:
            count += r - l
            l += 1
        else:
            r -= 1
    return count
print(count_pairs([-1, 1, 2, 3, 1], 2))        
print(count_pairs([-6, 2, 5, -2, -7, -1, 3], -2))
print(count_pairs([1, 1, 1, 1], 3))
print(count_pairs([1, 2, 3, 4, 5], 7))
print(count_pairs([10, 8, 5, 2, 1], 10))
print(count_pairs([1, 2, 3], 2))
print(count_pairs([10, 20, 30], 100))
print(count_pairs([], 10))
print(count_pairs([5], 0))
print(count_pairs([5, 1, 2], 0))
print(count_pairs([-2, 0, 1, 3], 2))
     