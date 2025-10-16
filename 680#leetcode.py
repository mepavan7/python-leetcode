def valid_palindrome_two(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            one = s[l+1 : r+1]
            two = s[l : r]
            return one == one[::-1] or two == two[::-1]
        l += 1
        r -= 1
    return True
print(valid_palindrome_two("aba"))
print(valid_palindrome_two("abca"))
print(valid_palindrome_two("abc"))

        
        
    
    































            