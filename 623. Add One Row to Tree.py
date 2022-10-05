'''iven the root of a binary tree and two integers val and depth, add a row of nodes with value val at the given depth depth.

Note that the root node is at depth 1.

The adding rule is:

Given the integer depth, for each not null tree node cur at the depth depth - 1, create two tree nodes with value val as cur's left subtree root and right subtree root.
cur's original left subtree should be the left subtree of the new left subtree root.
cur's original right subtree should be the right subtree of the new right subtree root.
If depth == 1 that means there is no depth depth - 1 at all, then create a tree node with value val as the new root of the whole original tree, and the original tree is the new root's left subtree.
 

Example 1:


Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]'''


class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            return TreeNode(v, left=root)
        self.addOneRowHelper(root, v, d, 1)
        return root
        
        
    def addOneRowHelper(self, root, v, d, level):    
        if d-1 == level:
            leftTree = TreeNode(v, left=root.left)
            rightTree = TreeNode(v, right=root.right)
            
            root.left = leftTree
            root.right = rightTree
            return
        
        if root.left:
            self.addOneRowHelper(root.left, v, d, level+1)
        if root.right:
            self.addOneRowHelper(root.right, v, d, level+1)
