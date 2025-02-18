# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x, length = head, 0
        while x != None:
            x=x.next
            length+=1
        x=head
        for i in range(0, length//2):
            x=x.next
        return x