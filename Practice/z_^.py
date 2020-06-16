class Solution:
    def singleNumber(self, nums):
        a = 0
        for num in nums:
            a = a ^ num 
        return a

test = Solution()
print(test.singleNumber([1,2,3,4,5,5,4,3,1]))