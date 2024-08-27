# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        add_one = 0
        while l1 or l2:
            total = add_one
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            add_one = total // 10
            total = total % 10
            curr.next = ListNode(total)
            curr = curr.next
        if add_one:
            curr.next = ListNode(add_one)
        return dummy.next

"""
l1: 1 -> 4 -> 3
l2: 9 -> 5 -> 6
    0    0    0   1

 341
 957
1000
add_one = 1
l1: 1 -> 4 -> 3
l2: 9 -> 5 -> 6
    0    0    0 
head c   c    c
if add_one:
    c.next = node(add_one)
return head

add_one = 1
l1: 1 -> 4
l2: 9 -> 5 -> 6
    0    0
headc    c
c.next = l2.next
"""