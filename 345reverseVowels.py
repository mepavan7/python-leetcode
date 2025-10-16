def reverse_vowels_string(s):
    s = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l].lower() in vowels:
                l += 1
                continue
            
        if s[r].lower() not in vowels:
            r -= 1
            continue
        
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1
    return "".join(s)
print(reverse_vowels_string("IceCreAm"))            
print(reverse_vowels_string("leetcode"))            