# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(val=-1)
        # while loop if A and B exist:
        while A and B:
            # compare A and B: assign smaller one to curr
            if A.val <= B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next
        if A:
            curr.next = A
        if B:
            curr.next = B
        return dummy.next
"""
list1 = [1,2,4], 
list2 = [1,3,4]
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
Time: O(n + m)
space: O(1)
"""