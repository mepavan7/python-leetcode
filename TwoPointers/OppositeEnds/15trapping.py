def trappingrainwater(height):
    l = 0
    r = len(height) - 1
    left_max = 0
    right_max = 0
    total_water = 0
    while l < r:
        if height[l] < height[r]:
            left_max = max(left_max,height[l])
            total_water += left_max - height[l]
            l += 1
        else:
            right_max = max(right_max, height[r])
            total_water += right_max - height[r]
            r -= 1
    return total_water
print(trappingrainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
            
            
        