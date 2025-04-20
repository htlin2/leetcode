class Node:
    def __init__(self, key=-1, val=-1):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None
        self.count = 1

class LFUCache:

    def __init__(self, cap: int):
        # {key: node}
        # {count: {head: node, tail: node}}
        #                       LRU
        self.cap = cap
        self.key_node_map = {}
        self.count_node_map = {}
        self.total_nodes = 0
    
    def remove_node(self, node):
        prev_node, next_node = node.prev, node.next
        if prev_node.val == -1 and next_node.val == -1:
            del self.count_node_map[node.count]
        else:
            prev_node.next, next_node.prev = next_node, prev_node
        del self.key_node_map[node.key]
        self.total_nodes -= 1

    def insert_node(self, node):
        self.key_node_map[node.key] = node
        if node.count not in self.count_node_map:
            head_node, tail_node = Node(-1), Node(-1)
            head_node.next, tail_node.prev = tail_node, head_node
            self.count_node_map[node.count] = {'head': head_node, 'tail': tail_node}
        head_tail_hashmap = self.count_node_map[node.count]
        head_node = head_tail_hashmap['head']
        next_node = head_node.next
        head_node.next, node.prev = node, head_node
        next_node.prev, node.next = node, next_node
        self.total_nodes += 1
        return node

    def get(self, key: int) -> int:
        if key not in self.key_node_map: return -1
        node = self.key_node_map[key]
        self.remove_node(node)
        node.count += 1
        self.insert_node(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        # if key is found:
        if key in self.key_node_map:
            # get node from key
            self.get(key)
            node = self.key_node_map[key]
            node.val = value
            return
        elif self.total_nodes == self.cap:
            # if cap is reached:
            # remove LRU node based on lowest count
            min_key = min(self.count_node_map)
            LRU_node = self.count_node_map[min_key]['tail'].prev
            self.remove_node(LRU_node)
        # insert new node in key:node
        node = Node(key, value)
        # insert new node to count next to head
        self.insert_node(node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)