class Solution(object):
    def romanToInt(self, s):
        total = 0
        i = 0
        while i != len(s):
            if (i + 1) != len(s):
                if self.converFromRoman(self, s[i]) < self.converFromRoman(self, s[i + 1]):
                    total -= 2 * self.converFromRoman(self, s[i])
            i += 1

        for char in s:
            total += self.converFromRoman(self, char)
        return total

    def converFromRoman(self, char):
        if char == "M":
            return 1000
        elif char == "D":
            return 500
        elif char == "C":
            return 100
        elif char == "L":
            return 50
        elif char == "X":
            return 10
        elif char == "V":
            return 5
        elif char == "I":
            return 1
        else:
            return 0

s = Solution
print(s.romanToInt(s, "LXIX"))
