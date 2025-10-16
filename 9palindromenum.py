def palindrome_number(x):
    s = str(x)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True
print(palindrome_number(121))
print(palindrome_number(-121))
print(palindrome_number(10))