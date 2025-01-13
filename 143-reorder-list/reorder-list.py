# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        dummy = ListNode(-1)
        dummy.next = head
        slow, fast = dummy, dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        A = head
        B = mid.next
        mid.next = None
        # reverse B
        prev, curr = None, B
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        B = prev
        dummy = curr = ListNode(-1)
        while A and B:
            curr.next = A
            curr = curr.next
            A = A.next
            curr.next = B
            curr = curr.next
            B = B.next
        curr.next = A
        return dummy.next
"""
find middle
reverse linkedlist
build list with reversed and normal

Input: head = [1,2,3,4]
  [ 1, 2, 3, 4]
sf sf sf  f  f

  [ 1, 2, 3, 4, 5]
sf sf sf sf  f  f 
"""