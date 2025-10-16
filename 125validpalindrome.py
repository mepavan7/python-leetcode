def valid_palindrome(s):
    filter = [char for char  in s.lower() if char.isalnum()]
    res = "".join(filter)
    l = 0
    r = len(filter) - 1
    while l < r:
        if filter[l] != filter[r]:
            return False
        l += 1
        r -= 1
    return True
print(valid_palindrome("A man, a plan, a canal: Panama"))
print(valid_palindrome("race a car"))
print(valid_palindrome(" "))
    