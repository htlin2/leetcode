# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, A: Optional[ListNode], B: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(-1)
        carry = 0
        while A or B:
            A_val, B_val = 0, 0
            if A:
                A_val = A.val
                A = A.next
            if B:
                B_val = B.val
                B = B.next
            combined = A_val + B_val + carry # 14
            carry = combined // 10 # 14 // 10 => 1
            curr.next = ListNode(combined % 10) # 14 % 10 => 4
            curr = curr.next
        if carry:
            curr.next = ListNode(carry)
        return dummy.next