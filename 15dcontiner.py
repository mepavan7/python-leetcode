def max_area(h):
    l , r = 0, len(h) - 1
    best = 0
    while l < r:
        area = min(h[l], h[r]) * (r - l)
        best = max(best, area)
        if h[l] < h[r]:
             l += 1
        else:
            r -= 1
    return best
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))