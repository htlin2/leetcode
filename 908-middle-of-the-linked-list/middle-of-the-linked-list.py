# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        return slow

"""
  1,  2,  3,  4,  5]
 sf  sf  sf   f   f

  1,  2,  3,  4,  5,  6
 sf  sf  sf   sf   f  f
"""