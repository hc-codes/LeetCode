// Problem: Word Search
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/word-search/
// Date: 2024-11-17

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(i,j,c,res):
            if c==len(word):
                return True
            
            if i>=len(board) or j>=len(board[0]) or i<0 or j<0 or board[i][j]!=word[c] or board[i][j]=='#':
                return False
            
            char=board[i][j]
            board[i][j]='#'
            # right
            right = search(i,j+1,c+1,res)
            # left
            left = search(i,j-1,c+1,res)
            # up
            up = search(i-1,j,c+1,res)
            # down
            down = search(i+1,j,c+1,res)
            
            board[i][j]=char # undo
            
            return left or right or up or down
            
        m=len(board)
        n=len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if search(i,j,0,""):
                        return True
        return False
        