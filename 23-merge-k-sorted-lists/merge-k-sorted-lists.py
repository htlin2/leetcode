# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def merge(self, A, B):
        dummy = curr = ListNode(-1)
        while A and B:
            if A.val <= B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next
        if A:
            curr.next = A
        if B:
            curr.next = B
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        if len(lists) == 1: return lists[0]
        res = []
        for i in range(0, len(lists), 2):
            A = lists[i]
            B = lists[i + 1] if i + 1 < len(lists) else None
            merged = self.merge(A, B)
            res.append(merged)
        return self.mergeKLists(res)

"""
recurrsion + merge

"""