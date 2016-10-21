class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
        chari = 0
        lngst = 0
        char = ""
        allgood = True
        while True:
            if len(strs[0]) > lngst:
                char = strs[0][chari]
            else:
                pass

            for string in strs:
                if len(string) <= lngst:
                    allgood = False
                    break
                if char != string[chari]:
                    allgood = False
                    break

            if allgood:
                chari += 1
                lngst += 1
            else:
                break

        prefix = ""
        for char in strs[0]:
            if lngst == 0:
                return prefix
            prefix += char
            lngst -= 1

        return prefix
s = Solution
print(s.longestCommonPrefix(s, []))
