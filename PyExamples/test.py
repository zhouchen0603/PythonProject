"""
Find how many "BALLOON" can be created from a string
Example:
    BALLOON -> return 1
    BALLOONBALLOON -> return 2
    BBAALLLLOOOONN -> return 2
    AAAAABBBALLOONXXX -> return 1
    XXXX -> return 0
"""

import collections
class Solution:
    @classmethod
    def solution(self,S):
        table = collections.defaultdict(int)
        #print(table)
        for c in S:
            table[c] += 1
        ans = float('inf')
        for c in 'ABN':
            ans = min(ans, table[c])
        for c in 'LO':
            ans = min(ans, table[c])
        return ans

test = {"BALLOON": 1, "B": 0,"NOOLLAB":1,"XXXXBXAXLOOLNX":1}
for key in test.keys():
    res = Solution.solution(key)
    print(key+":"+str(res))