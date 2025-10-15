def boats_to_save(people, limit):
    people.sort()
    l = 0
    r = len(people) - 1
    count = 0
    while l <= r:
        if people[l] + people[r] <= limit:
            count += 1
            l += 1
            r -= 1
        else:
            count += 1
            r -= 1
    return count
print(boats_to_save([3, 2, 2, 1], 3))
            