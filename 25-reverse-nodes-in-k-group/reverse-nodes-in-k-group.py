# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def get_kth_node(self, node, k):
        while node and k > 1:
            k -= 1
            node = node.next
        return node

    def reverse(self, node):
        prev, curr = None, node
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev, node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth_node = self.get_kth_node(head, k)
        if not kth_node: return head
        A = head
        B = kth_node.next
        kth_node.next = None
        (reversed_A_head, reversed_A_tail) = self.reverse(A)
        reversed_A_tail.next = self.reverseKGroup(B, k)
        return reversed_A_head
"""
Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]

[1,2,3,4,5]
 i i i
dp = [1, 2] == k
dummy -> 2 -> 1 -> 

split into k group
    reverse k group
    curr -> revered k group
"""