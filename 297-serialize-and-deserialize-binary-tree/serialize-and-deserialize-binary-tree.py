# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        res = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if not node:
                res.append('N')
                continue
            res.append(str(node.val))
            q.append(node.left)
            q.append(node.right)
        return ','.join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        arr = data.split(',')
        i = 0
        root = TreeNode(int(arr[i]))
        q = collections.deque([root])
        while q:
            i += 1
            node = q.popleft()
            node.left = TreeNode(int(arr[i])) if arr[i] != 'N' else None
            if node.left:
                q.append(node.left)
            i += 1
            node.right = TreeNode(int(arr[i])) if arr[i] != 'N' else None
            if node.right:
                q.append(node.right)
        return root
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))