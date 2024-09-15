# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        while A or B:
            if A and B:
                if A.val <= B.val:
                    curr.next = A
                    A = A.next
                else:
                    curr.next = B
                    B = B.next
            elif A:
                curr.next = A
                A = A.next
            elif B:
                curr.next = B
                B = B.next
            curr = curr.next
        return dummy.next