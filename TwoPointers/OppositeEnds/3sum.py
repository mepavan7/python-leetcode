#Brtue Force
def threeSum(nums):
    res = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                
                if nums[i] + nums[j] + nums[k] == 0:
                   res.add((nums[i],nums[j],nums[k]))
    return list(res)
#print(threeSum([-1,0,1,2,-1,-4]))

#Opposite End
def threeSum(nums):
    n = len(nums)
    nums.sort() 
    total = 0
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total < 0:
                l += 1
            elif total > 0:
                r -=1
            else:
                res.append((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
                
                while l < r and nums[l] == nums[l-1]:
                    l += 1    
                
                while l < r and nums[r] == nums[r+1]:
                   r -= 1
           
    return res

print(threeSum([-1,0,1,2,-1,-4]))
                
            