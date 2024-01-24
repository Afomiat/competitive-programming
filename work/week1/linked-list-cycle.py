# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        L_set = set()
        cur = head
        while cur != None:
            if cur.next in L_set:
                return True
            else:
                L_set.add(cur.next)
                cur = cur.next
                
        return False
       

     
        