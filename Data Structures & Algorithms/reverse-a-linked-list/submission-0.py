# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = newhead
            newhead = curr # make the new head tranverse one ,this way the next node cna d teh same peration
            curr = temp

        return newhead