# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        if not A: return B
        if not B: return A
        (small, large) = (A, B) if A.val <= B.val else (B, A)
        small.next = self.mergeTwoLists(small.next, large)
        return small
"""
list1 = [1,2,4], 
list2 = [1,3,4]
dummy -> 1 -> 1 -> 2 -> 3 -> 4 -> 4
Time: O(n + m)
space: O(1)
"""