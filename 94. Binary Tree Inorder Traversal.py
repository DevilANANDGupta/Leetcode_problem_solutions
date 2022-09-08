'''
Given the root of a binary tree, return the inorder traversal of its nodes' values.
Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]'''

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        ans = []
        if not root: return
        
        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            ans.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return ans
