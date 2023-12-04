def shortestPalindrome(s: str) -> str:
    i = 0
    for j in range(len(s) - 1, -1, -1):
        if s[i] == s[j]:
            i += 1

    return s[i:][::-1] + s


s1 = "aacecaaa"
result1 = shortestPalindrome(s1)
print(result1)  

s2 = "abcd"
result2 = shortestPalindrome(s2)
print(result2)  
