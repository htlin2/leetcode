from collections import deque
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
        ans = []
        q = deque([root])
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if not node:
                    ans.append('N')
                    continue
                ans.append(str(node.val))
                left, right = node.left, node.right
                q.append(left)
                q.append(right)
        return ','.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        i = 0
        if data[i] == 'N': return None
        ans = TreeNode(int(data[i]))
        q = deque([ans])
        while q:
            node = q.popleft()
            if not node: continue
            i += 1
            left = None if data[i] == 'N' else TreeNode(int(data[i]))
            node.left = left
            q.append(left)

            i += 1
            right = None if data[i] == 'N' else TreeNode(int(data[i]))
            node.right = right
            q.append(right)
        return ans

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))