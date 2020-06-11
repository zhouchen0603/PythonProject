#[[1,0],[2,2],[3,4]]
#(0,0)  -> K

class Solution:

    def find_k_points2(self, point_arr, k):
        point_arr = sorted(point_arr, key=lambda point: abs(point[0]) + abs(point[1]))
        print(point_arr)

        return point_arr[:k]

    def find_k_points(self, point_arr, k):
        i,j=0,len(point_arr)-1
        acc = 0
        max_acc = 0
        res = []
        while(i<j):
            acc = abs(point_arr[i][0]) + abs(point_arr[i][1])
            acc1 = abs(point_arr[j][0]) + abs(point_arr[j][1])
            if acc > acc1:
                point_arr[i], point_arr[j] = point_arr[j], point_arr[i]


        print(point_arr)
        return point_arr[:k]

    def print_link_list(self, root):
        stack = [root]
        res = []
        while(len(stack)>0):
            stack2 = []
            for i in range(len(stack)):
                res.append(stack[i].val)
                if root.left:
                    stack2.append(stack[i].left)
                if root.right:
                    stack2.append(stack[i].right)
            stack = stack2
        return res

class LinkList:

    def __init__(self, val, left=None, right=None):
        self._val = val
        self._left = left
        self._right = right





test = Solution()
print(test.find_k_points([(3,4),(1,0),(0,1),(2,2)], 2))

