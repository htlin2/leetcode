# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head: return True
        # find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next        
        # reverse second half
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        B = prev
        A = head
        # compare first and second
        while A and B:
            if A.val != B.val: return False
            A = A.next
            B = B.next
        return True
"""
even
[1, 2, 2, 1]
sf,sf,sf, f f
odd
[1, 2, 1]
sf,sf,sf, f

"""