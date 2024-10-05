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
        res = []
        def dfs(node):
            if node:
                res.append(str(node.val))
            else:
                res.append('N')
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_arr = data.split(',')
        i = -1
        def dfs():
            nonlocal i
            i += 1
            if i >= len(data_arr): return None
            val = data_arr[i]
            if val == 'N': return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

"""
post order dfs
1,2,N,N,3,4,N,N,5,N,N
         1
       2
    N
      0
    1 0*2+1    2 0*2+2
  3 1*2+1   4 1*2+2  5 2*2+1 6 2*2+2
7 3*2+1 8 3*2+2
""" 