# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        set_l = set()
       
        cur = head
        while cur:
            if cur in set_l:
                return cur
            else:
                set_l.add(cur)
                cur = cur.next
       