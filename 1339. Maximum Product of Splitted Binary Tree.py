# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:    
        def count(node: TreeNode) -> int:
            if not node: return 0, 0
            left_so_far, left = count(node.left)
            right_so_far, right = count(node.right)
            current = node.val + left + right
            max_so_far = max(left_so_far, right_so_far, (total - current) * current)
            return max_so_far, current
        total = 0
        _, total = count(root)
        return count(root)[0] % (10 ** 9 + 7)
