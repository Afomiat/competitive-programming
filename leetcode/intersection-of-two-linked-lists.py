# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_a = set()
      
        cur_a, cur_b = headA, headB
        while cur_a:
            set_a.add(cur_a)
            cur_a = cur_a.next
        while cur_b:
            if cur_b in set_a:
                return cur_b
            set_a.add(cur_b)
            cur_b = cur_b.next
        
        return None