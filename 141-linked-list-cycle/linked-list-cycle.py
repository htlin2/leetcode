# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False
        hashmap = {}
        node = head
        while node:
            if node in hashmap: return True
            hashmap[node] = node
            node = node.next
        return False

"""
[ 3, 2, 0, -4], pos = 1
 sf,sff,sff, fsf
"""