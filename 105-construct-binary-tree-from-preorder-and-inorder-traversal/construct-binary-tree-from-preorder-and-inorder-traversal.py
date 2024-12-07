# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        node = TreeNode(preorder[0])
        idx = inorder.index(node.val)
        node.left = self.buildTree(preorder[1:idx + 1], inorder[:idx])
        node.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return node

"""
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
preorder = [3,9,20,15,7]
            n l  n
inorder = [9,3,15,20,7]
           l n r

         3
        / \
       9   20
      / \  / \ 
     1  2 15 7
out: [3,9,20,1,2,15,7]
preorder = [3,9,1,2,20,15,7]
            n n 
inorder =  [1,9,2,3,15,20,7]
              n   n
def dfs(preorder, inorder):
    node = preorder[0]
    idx = find node.val in inorder
    node.left = dfs([1:4 idx + 1](9-2), [0:3 idx](1-2))
    node.right = dfs([], [idx+1:])
    return node


"""