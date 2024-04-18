class Node:
    def __init__(self, key=-1, next=None, prev=None):
        self.key = key
        self.next = next
        self.prev = prev

class LL:
    def __init__(self):
        head, tail = Node(), Node()
        head.next, tail.prev = tail, head
        self.head = head
        self.tail = tail
        self.key_node_map = {}
    
    def add(self, prev_node, curr_node, next_node):
        prev_node.next, next_node.prev = curr_node, curr_node
        curr_node.next, curr_node.prev = next_node, prev_node
        self.key_node_map[curr_node.key] = curr_node
        return curr_node.key

    def add_head(self, key):
        prev_node = self.head
        curr_node = Node(key)
        next_node = self.head.next
        return self.add(prev_node=prev_node, curr_node=curr_node, next_node=next_node)

    def pop(self, key):
        if key not in self.key_node_map: return -1
        curr_node = self.key_node_map[key]
        prev_node, next_node = curr_node.prev, curr_node.next
        prev_node.next, next_node.prev = next_node, prev_node
        del self.key_node_map[key]
        return key

    def pop_tail(self):
        return self.pop(key=self.tail.prev.key)

    def length(self):
        return len(self.key_node_map)

class LFUCache:
    def __init__(self, cap: int):
        self.cap = cap
        self.lfu_count = 0
        self.key_val_map = collections.defaultdict(int)
        self.key_count_map = collections.defaultdict(int)
        self.count_ll_map = collections.defaultdict(LL)

    def counter(self, key):
        count = self.key_count_map[key]
        self.key_count_map[key] += 1
        self.count_ll_map[count].pop(key)
        self.count_ll_map[count + 1].add_head(key)

        if self.lfu_count == count and self.count_ll_map[count].length() == 0:
            self.lfu_count += 1


    def get(self, key: int) -> int:
        if key not in self.key_val_map: return -1
        self.counter(key)
        return self.key_val_map[key]

    def put(self, key: int, val: int) -> None:
        if self.cap == 0: return
        # remove lfu
        if key not in self.key_val_map and self.cap == len(self.key_val_map):
            lfu_key = self.count_ll_map[self.lfu_count].pop_tail()
            del self.key_val_map[lfu_key]
            del self.key_count_map[lfu_key]

        self.key_val_map[key] = val
        self.counter(key)
        self.lfu_count = min(self.lfu_count, self.key_count_map[key])

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)