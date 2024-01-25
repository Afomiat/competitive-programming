# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
class Solution:
    def __init__(self):
        self.head = None
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = list1
        p2 = list2
        last = None
        if not p1 and not p2:
            return p1
        elif not p1:
            return p2
        elif not p2:
            return p1
        while p1 and p2:
            if p1.val == p2.val:
                node1 = Node(p1.val)
                node2 = Node(p2.val)

                # self.head = node1
                # node1.next = node2
                p1 = p1.next
                p2 = p2.next
                if last:
                    last.next = node1
                else:
                    self.head = node1
                node1.next = node2
                last = node2
            elif p1.val < p2.val:
                node1 = Node(p1.val)
                if last:
                    last.next = node1
                else:
                    self.head = node1
                last = node1
                
                p1 = p1.next
                # print(self.head.val)
            else:
                node2 = Node(p2.val)
                if last:
                    last.next = node2
                else:
                    self.head = node2
                last = node2
                p2 = p2.next
                # print(self.head.val)
        if p1:
            last.next = p1
        if p2:
            last.next = p2

        return self.head



