# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
"""
1 brute force
get all val in linked list
reverse val 
create a new linked list with val
Time: O(n)
Space: O(n)

2 two pointers
using a temp variables to hold node
reassign with current to next and previous to current
Time: O(n)
Space: O(1)
"""