"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy_hashmap = {-1: Node(-1), None: None} # original_node: copy_node
        dummy = copy_hashmap[-1]
        curr = head
        while curr:
            # handle copy
            if curr in copy_hashmap:
                copy_node = copy_hashmap[curr]
            else:
                copy_node = Node(curr.val)
                copy_hashmap[curr] = copy_node
            dummy.next = copy_node
            # handle random
            if curr.random in copy_hashmap:
                random_node = copy_hashmap[curr.random]
            else:
                random_node = Node(curr.random.val)
                copy_hashmap[curr.random] = random_node
            copy_node.random = random_node
            dummy = dummy.next
            curr = curr.next
        return copy_hashmap[-1].next


"""
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]] => [node.val, index]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

hashmap = {
    index: node
        0: node(7)
        1: node(13)
        2: node(11)
        3: node(10)
        4: node(1)
} 
dummy : 7    ->        13  ->  hashmap[2]
random: null -> hashmap[0] ->  hashmap[4]

Time: O(n)
Space: O(n)
"""