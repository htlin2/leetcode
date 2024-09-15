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
        slow = fast = head
        fast = fast.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        B = slow.next
        slow.next = None
        # reverse B
        prev = None
        while B:
            temp = B.next
            B.next = prev
            prev = B
            B = temp
        B = prev
        A = head
        # merge A and B
        dummy = curr = ListNode(-1)
        while A and B:
            curr.next = A
            A = A.next
            curr = curr.next

            curr.next = B
            B = B.next
            curr = curr.next
        if A:
            curr.next = A
        if B:
            curr.next = B
        return dummy.next
"""
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]

odd, s stops at 2
 d  1  2  3  4  5
 s sf  s  f     f
even,  2
 d  1  2  3  4
 s sf  s  f    f
A = 1 2 3
B = 4 5
reverse(B)
B = 5 4 3

"""