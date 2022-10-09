'''Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:   
        
        values = []
        self.inorder_traverse(root, values)

        left = 0
        right = len(values) - 1
        
        while left < right:
            if values[left] + values[right] < k:
                left += 1
            elif values[left] + values[right] > k:
                right -= 1
            else:
                return True
                    
        return False

        
    def inorder_traverse(self, root, results):
        if not root:
            return
        
        self.inorder_traverse(root.left, results)
        results.append(root.val)
        self.inorder_traverse(root.right, results)
