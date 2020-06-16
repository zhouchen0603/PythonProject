class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def create_tree(self, val_list):
        root = None
        if(len(val_list)==0):
            return None
        else:
            root = TreeNode(val_list[0])
        i = 1
        node_list = [root]
        while(i<len(val_list)):
            cur = node_list[0]
            node_list = node_list[1:]
            if cur:
                if val_list[i]:
                    cur.left = TreeNode(val_list[i])
                    node_list.append(cur.left)
                    i = i + 1
                    if i >= len(val_list):
                        break
                else:
                    i = i + 1
                    if i >= len(val_list):
                        break
                if val_list[i]:
                    cur.right = TreeNode(val_list[i])
                    node_list.append(cur.right)
                    i = i + 1
                    if i >= len(val_list):
                        break
                else:
                    i = i + 1
                    if i >= len(val_list):
                        break
        return root

    def print_tree(self, root):
        stack = [root]
        res = []
        while(len(stack)>0):
            stack2 = []
            res1 = []
            for node in stack:
                if node:
                    print(node.val)
                    res1.append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    else:
                        stack2.append(None)
                    if node.right:
                        stack2.append(node.right)
                    else:
                        stack2.append(None)
            if(len(res1)>0):
                res.append(res1)
            stack = stack2
        print(res)
        return res



    def levelOrder(self, root):
        stack = [root]
        res = []
        while(len(stack)>0):
            stack2 = []
            res1 = []
            for node in stack:
                if node:
                    print(node.val)
                    res1.append(node.val)
                    if node.left:
                        stack2.append(node.left)
                    if node.right:
                        stack2.append(node.right)
            if(len(res1)>0):
                res.append(res1)
            stack = stack2
        print(res)
        return res

test = Solution()
tree = test.create_tree([3,9,20,None,None,15,7])
test.print_tree(tree)
test.levelOrder(tree)