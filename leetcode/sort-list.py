# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def helper(arr):
            if not arr:
                return None
           
            dummy = ListNode(arr[0])
            cur = dummy
            
            for i in range(1, len(arr)):
                new_node =ListNode(arr[i])
                cur.next = new_node
                cur = new_node
            return dummy

        arr = []
        curr = head
       
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr.sort()

        return helper(arr)




      