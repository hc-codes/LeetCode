// Problem: Maximum Depth of Binary Tree
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// Date: 2023-08-25

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack=[root]
        value=[1]
        depth=0
        while stack:
            node = stack.pop()
            temp = value.pop()
            depth = max(temp,depth)
            if(node.left):
                stack.append(node.left)
                value.append(temp+1)
            if(node.right):
                stack.append(node.right)
                value.append(temp+1)
        return depth