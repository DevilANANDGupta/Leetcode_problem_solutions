#User function Template for python3

'''class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''
class Solution:
    def deleteNode(self,head, x):
        cur=head
        count = 1
        while count != x:
            cur = cur.next
            count +=1
        prev = cur.prev
        next=cur.next
        if prev:
            prev.next=next
        if next:
            next.prev=prev
