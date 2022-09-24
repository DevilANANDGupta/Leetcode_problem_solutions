'''Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []
Example 3:

Input: root = [1,2], targetSum = 0
Output: []'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        if not root.left and not root.right and targetSum == root.val:
            return [[root.val]]
        l_path = self.pathSum(root.left, targetSum-root.val)
        r_path = self.pathSum(root.right, targetSum-root.val)
        left = [[root.val]+l for l in l_path]
        right = [[root.val]+r for r in r_path]
        return left+right
    
# other solution
class Solution:
    def pathSum(self, root, sum):
      return self._pathSum(root, sum, [], [])

    def _pathSum(self, root, sum, path, result):
      if root is None:
        return result

      if sum == root.val and root.left is None and root.right is None:
        return result + [path + [root.val]]
      else:
        return self._pathSum(root.left, sum - root.val, path + [root.val], result) + self._pathSum(root.right, sum - root.val, path + [root.val], result)

        
