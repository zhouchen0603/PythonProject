#[1,2,3,2]
# target=4
import collections

class Solution:

    def sub_arr(self, arr, target, k):
        res = []
        if k>len(arr):
            return None
        if k==1:
            if target in arr:
                return [[target]]
            else:
                return None
        if k==len(arr) and sum(arr) == target:
            return arr
        for i in range(len(arr)):
            arr2 = self.sub_arr(arr[i+1:], target - arr[i], k-1)
            if arr2 != None:
                for a in arr2:
                    res.append([arr[i]]+a)
        if len(res) == 0:
            return None
        return res

test = Solution()
print(test.sub_arr([1,2,3,4,5,6,7,8,9], 15, 3))

