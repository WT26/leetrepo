class Solution(object):
    def myAtoi(self, str):
        minus_added = False
        plus_added = False
        first_number = False
        string_to_convert = ""
        for char in str:
            if char == "1" or char == "2" or char == "3" or char == "4" or \
                            char == "5" or char == "6" or char == "7" or\
                            char == "8" or char == "9" or char == "0":
                first_number = True
                string_to_convert += char
            elif char == "-" and not minus_added and not plus_added:
                first_number = True
                minus_added = True
            elif char == "+" and not minus_added and not plus_added:
                first_number = True
                plus_added = True
            elif first_number == False and char == " ":
                pass
            else:
                break

        if len(string_to_convert) > 1:
            for char in string_to_convert:
                if char == "0":
                    string_to_convert = string_to_convert[1:]
                else:
                    break
        if len(string_to_convert) <= 0:
            return 0
        if minus_added:
            string_to_convert = "-" + string_to_convert
        if plus_added:
            string_to_convert = "+" + string_to_convert

        if int(string_to_convert) > 2147483647:
            return 2147483647
        elif int(string_to_convert) < -2147483648:
            return -2147483648
        return int(string_to_convert)
s = Solution
print(s.myAtoi(s, "   - 321"))