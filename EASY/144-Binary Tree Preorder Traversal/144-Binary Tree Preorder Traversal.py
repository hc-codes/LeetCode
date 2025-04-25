// Problem: Binary Tree Preorder Traversal
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/binary-tree-preorder-traversal/
// Date: 2025-04-24

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right) if root else []
        