class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)  
        dummy.next = head
        pre_left = dummy
        
        
        for _ in range(left - 1):
            pre_left = pre_left.next
        
        prev = None
        curr = pre_left.next
       
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
       
        pre_left.next.next = curr
        pre_left.next = prev
        
        return dummy.next