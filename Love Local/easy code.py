class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        while i >= 0 and s[i] == ' ':
            i -= 1
        j = i
        while j >= 0 and s[j] != ' ':
            j -= 1
        return i - j  

# Test cases
solution = Solution()

s1 = "Hello World"
print(solution.lengthOfLastWord(s1),s1)

s2 = "fly me   to   the moon"
print(solution.lengthOfLastWord(s2),s2)  

s3 = "luffy is still joyboy"
print(solution.lengthOfLastWord(s3),s3) 
