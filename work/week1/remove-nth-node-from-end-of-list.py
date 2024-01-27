# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverse(head):
            prev = None
            cur = head

            while cur:
                new_node = cur.next
                cur.next = prev
                prev = cur
                cur = new_node
            return prev

        def delete(node, n):
            if n == 1:
                return node.next
            temp = node
            for i in range(n - 2):
                temp = temp.next
            if temp.next is not None:
                temp.next = temp.next.next
            
            return node



        rev = reverse(head)
        delt = delete(rev, n)
        result = reverse(delt)

        return result