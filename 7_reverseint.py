class Solution(object):
    def reverse(self, x):
        string_of_number = str(x)
        rearranged = ""
        add_minus = False
        for char in string_of_number:
            if char == "-":
                add_minus = True
            else:
                rearranged = char + rearranged
        if len(rearranged) > 1:
            print(rearranged)
            for char in rearranged:
                if char == "0":
                    rearranged = rearranged[1:]
                else:
                    break
        if add_minus:
            rearranged = "-" + rearranged
        if int(rearranged) > 2147483647 or int(rearranged) < -2147483647:
            return 0
        return int(rearranged)

s = Solution
print(s.reverse(s, 0))