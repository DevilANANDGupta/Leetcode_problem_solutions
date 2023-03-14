def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        res = 0
        arr = []
        def dfs(root, res):
            if root is None: return
            if not root.left and not root.right:
                arr.append(res+root.val)
                return
            dfs(root.left, (res+root.val)*10)
            dfs(root.right, (res+root.val)*10)
        dfs(root, res)
        return sum(arr)
