class Solution(object):
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

s = Solution
print(s.isPalindrome(s, "2147483648463847412"))
