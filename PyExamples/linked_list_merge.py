# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def print_list_node(l):
    arr = []
    while(l):
        arr.append(l.val)
        l = l.next
    print(arr)

def create_sorted_list_node(arr):
    l1 = last = None
    arr = sorted(arr)
    for val in arr:
        # print_list_node(l1)
        if l1 == None:
            l1 = last = ListNode(val)
        else:
            last.next = ListNode(val)
            last = last.next
    return l1

class Solution:
    #def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    @classmethod
    def mergeTwoLists(self, l1, l2):
        while(l1 and l2):
            new_head = None
            if l1.val <= l2.val:
                new_head = ListNode(l1.val)
                new_head.next = self.mergeTwoLists(l1.next, l2)
            else:
                new_head = ListNode(l2.val)
                new_head.next = self.mergeTwoLists(l1, l2.next)
            return new_head
        else:
            return l1 if l1 else l2

l1 = create_sorted_list_node([1, 4, 6,3])
l2 = create_sorted_list_node([2,6,1])

print_list_node(Solution.mergeTwoLists(l1,l2))
