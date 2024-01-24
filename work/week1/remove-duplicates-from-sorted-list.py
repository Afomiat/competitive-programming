# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        L_set = set()
        temp = head

        while temp:
            if temp.val in L_set:
                prev.next = temp.next
            else:
                prev = temp
            L_set.add(temp.val)
            temp = temp.next
        return head