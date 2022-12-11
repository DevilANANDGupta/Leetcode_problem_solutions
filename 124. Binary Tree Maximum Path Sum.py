# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -10**20
        # res=[root.val]
        # best = -float("inf")
        def maxPath(node):
            if not node:
                return 0
            left = maxPath(node.left)
            right= maxPath(node.right)
            leftMax = max(left, 0)
            rightMax = max(right,0)
            res=( node.val + leftMax+rightMax)
            nonlocal best
            best = max(res, best)

            return node.val + max(max(left, right),0)
        maxPath(root)
        return (best)
