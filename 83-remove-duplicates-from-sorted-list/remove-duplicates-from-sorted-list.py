# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        linkedlist = head
        if head is None:
            return head
        while linkedlist.next:
            if linkedlist.val == linkedlist.next.val:
                linkedlist.next = linkedlist.next.next
            else:
                linkedlist = linkedlist.next
        return head