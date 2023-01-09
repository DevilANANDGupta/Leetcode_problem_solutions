# Recursive

class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    ans = []

    def preorder(root: Optional[TreeNode]) -> None:
      if not root:
        return

      ans.append(root.val)
      preorder(root.left)
      preorder(root.right)

    preorder(root)
    return ans
  
#   Time: O(n)O(n)
# Space: O(n)O(n)

# Iterative
class Solution:
  def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
      return []

    ans = []
    stack = [root]

    while stack:
      node = stack.pop()
      ans.append(node.val)
      if node.right:
        stack.append(node.right)
      if node.left:
        stack.append(node.left)

    return ans
