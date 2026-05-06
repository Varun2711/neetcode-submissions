# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def inOrder(node, res):

            if not node:
                return
            
            inOrder(node.left, res)
            res.append(node.val)
            inOrder(node.right, res)
            

        res = []
        inOrder(root, res)
        print(res)
        for i in range(1, len(res)):
            if res[i-1] >= res[i]:
                return False

        return True

            