class Solution(object):
    def isValid(self, s):
        if len(s) == 0:
            return True
        if len(s) % 2 != 0:
            return False
        else:
            i = 0
            openings = ""
            while True:
                if len(s) == i:
                    break
                char = s[i]
                if self.isOpening(self, char):
                    openings += char
                else:
                    if len(openings) == 0:
                        return False
                    elif self.getPair(self, openings[-1:]) == char:
                        openings = openings[:-1]
                    else:
                        return False
                i += 1
            if len(openings) != 0:
                return False
            return True

    def getPair(self, char):
        if char == "[":
            return "]"
        elif char == "{":
            return "}"
        elif char == "(":
            return ")"
        else:
            return "0"

    def isOpening(self, char):
        if char == "[":
            return True
        elif char == "{":
            return True
        elif char == "(":
            return True
        else:
            return False
s = Solution
print(s.isValid(s, "{[]()()[]}"))