# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        hashmap = collections.defaultdict(list)
        def dfs(node, level):
            if not node: return
            hashmap[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        ans = []
        for i in range(len(hashmap)):
            ans.append(hashmap[i])
        return ans