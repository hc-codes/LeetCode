// Problem: Copy List with Random Pointer
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/copy-list-with-random-pointer/
// Date: 2024-08-31

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        curr=head
        res=Node(-1)
        h2=res
        dic={}
        while curr:
            node=Node(curr.val)
            res.next=node
            dic[curr]=node
            res=res.next
            curr=curr.next
        curr=head
        res=h2
        res=res.next
        while curr:
            node=dic[curr.random] if curr.random in dic else None
            res.random=node
            curr=curr.next
            res=res.next
        return h2.next
            