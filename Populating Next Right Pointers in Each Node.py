class Solution:
   def connect(self,root):
        node=root
        while(root):
            
            childhead=None
            child=None
            while(root):
                if root.left:
                    if childhead is None:
                        childhead=root.left
                        child=root.left
                    else:
                        child.next=root.left
                        child=child.next
                if root.right:
                    if childhead is None:
                        childhead=root.right
                        child=root.right
                    else:
                        child.next=root.right
                        child=child.next
                root=root.next
            root=childhead
        return node
