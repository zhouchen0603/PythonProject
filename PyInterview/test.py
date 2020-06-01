import collections
class Solution:
    def solution(self,S):
        table = collections.defaultdict(int)
        print(table)
        for c in S:
            table[c] += 1
        ans = float('inf')
        for c in 'ABN':
            ans = min(ans, table[c])
        for c in 'LO':
            ans = min(ans, table[c])