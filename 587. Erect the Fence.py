class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def start(p1,p2,p3):
            return (p2[1]-p1[1])* (p3[0]-p1[0])-(p2[0]-p1[0])*(p3[1]-p1[1])
        def build(trees):
            stack=[]
            for i in trees:
                while len(stack)>=2 and start(stack[-2],stack[-1],i)<0:
                    stack.pop()
                stack.append(tuple(i))
            return stack
        trees.sort()
        leftToRight = build(trees)
        rightToLeft = build(trees[::-1])
        return list(set(leftToRight + rightToLeft))
        
