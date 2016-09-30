class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
         :rtype: str
        """
        list_of_strings = []
        index = 0
        ans = ""
        while index != numRows:
            list_of_strings.append("")
            index += 1
        cursor = 0
        counter = numRows
        up = False
        if numRows == 1:
            ans = s
        else:
            for char in s:
                list_of_strings[cursor] = list_of_strings[cursor] + char
                counter -= 1
                print(counter)
                if counter == 0:
                    up = not up
                    counter = numRows - 1
                if up:
                    cursor -= 1
                else:
                    cursor += 1

            ans = ""
            for string in list_of_strings:
                ans += string
        return ans

s = Solution
print(s.convert(s, "ABC", 1))