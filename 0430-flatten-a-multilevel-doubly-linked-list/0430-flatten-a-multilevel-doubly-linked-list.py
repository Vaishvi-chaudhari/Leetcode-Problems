"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        curr = head
        while curr:
            if curr.child:
                next_node = curr.next
                child_head = curr.child
                tail = child_head
                
                while tail.next:
                    tail = tail.next

                curr.next = child_head
                child_head.prev = curr
                curr.child = None

                if next_node:
                    tail.next = next_node
                    next_node.prev = tail
            curr = curr.next
        return head