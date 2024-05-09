# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create dummy node and link with head
        dummy = ListNode(val=-1, next=head)
        # slow pointer starts at dummy, fast starts at head
        slow, fast = dummy, head
        # while n: move fast forward and n -= 1
        while n:
            # if fast is None: return dummy.next
            if not fast: return dummy.next
            fast = fast.next
            n -= 1
        # while fast is valid:
        while fast:
            # move both slow and fast forward
            slow, fast = slow.next, fast.next
        # remove node by using slow.next
        slow.next = slow.next.next
        return dummy.next