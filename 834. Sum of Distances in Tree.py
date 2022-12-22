class Solution:
  def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
    ans = [0] * N
    count = [1] * N
    tree = collections.defaultdict(set)
    for u, v in edges:
      tree[u].add(v)
      tree[v].add(u)
    def postorder(node, parent=None):
      for child in tree[node]:
        if child == parent:
          continue
        postorder(child, node)
        count[node] += count[child]
        ans[node] += ans[child] + count[child]
    def preorder(node, parent=None):
      for child in tree[node]:
        if child == parent:
          continue
        ans[child] = ans[node] - count[child] + (N - count[child])
        preorder(child, node)
    postorder(0)
    preorder(0)
    return ans
