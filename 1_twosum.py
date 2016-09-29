class Solution(object):
    def twosum(self, nums, target):
        i1 = 0
        for first_number in nums:
            number_to_find = target - first_number
            if number_to_find in nums:
                i2 = nums.index(number_to_find)
                if i1 != i2:
                    #print(i1, i2)
                    return i1, i2
            i1 += 1

#c = Solution
#c.twosum(c, [3,2,4], 6)