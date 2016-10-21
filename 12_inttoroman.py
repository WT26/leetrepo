class Solution(object):
    def intToRoman(self, num):
        roman = ""
        thousands, remainder = divmod(num, 1000)
        roman += thousands * "M"

        if remainder >= 900:
            roman += "CM"
            remainder -= 900

        fivehundreds, remainder = divmod(remainder, 500)
        roman += fivehundreds * "D"

        if remainder >= 400:
            roman += "CD"
            remainder -= 400

        hundreds, remainder = divmod(remainder, 100)
        roman += hundreds * "C"

        if remainder >= 90:
            roman += "XC"
            remainder -= 90

        fiftys, remainder = divmod(remainder, 50)
        roman += fiftys * "L"

        if remainder >= 40:
            roman += "XL"
            remainder -= 40

        tens, remainder = divmod(remainder, 10)
        roman += tens * "X"

        if remainder >= 9:
            roman += "IX"
            remainder -= 9

        fives, remainder = divmod(remainder, 5)
        roman += fives * "V"

        if remainder >= 4:
            roman += "IV"
            remainder -= 4

        roman += remainder * "I"

        return roman



s = Solution
print(s.intToRoman(s, 3999))
