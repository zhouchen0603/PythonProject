
class Solution:

    def solution(self, supported_digits=[2,6]):
        if len(supported_digits)==0:
            raise Exception("Please provided at lease 1 number")
        max_res = 90 + max(supported_digits)
        min_res = 10 + min(supported_digits)

        print(max_res, min_res)


s = Solution()
s.solution(supported_digits=[2,6])
s.solution(supported_digits=[1,3,9])
s.solution(supported_digits=[1,3,0])


