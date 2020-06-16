tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
#Return ["JFK", "MUC", "LHR", "SFO", "SJC"]

tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#["JFK","ATL","JFK","SFO","ATL","SFO"].
class Solution:

    def covert(self, tickets):
        ti_dict = {}
        for i in range(len(tickets)):
            if tickets[i][0] in ti_dict.keys():
                ti_dict[tickets[i][0]].append(tickets[i][1])
            else:
                ti_dict[tickets[i][0]] = [tickets[i][1]]
        for key in ti_dict.keys():
            ti_dict[key] = sorted(ti_dict[key])
        return ti_dict

    def print_path(self, tickets, start):
        ti_dict = self.covert(tickets)
        print(ti_dict)
        res = [start]
        while(True):
            if res[-1] in ti_dict.keys() and len(ti_dict[res[-1]]) >0:
                ti_dict[res[-1]] = ti_dict[res[-1]]
                res.append(ti_dict[res[-1]][0])
                del ti_dict[res[-2]][0]
                #print(res)
                #print(ti_dict)
            else:
                break
        print(res)
        return res



test = Solution()
test.print_path(tickets1, start='JFK')
test.print_path(tickets2, start='JFK')

