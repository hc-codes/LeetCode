// Problem: Find the K-th Character in String Game I
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/
// Date: 2024-10-20

class Solution:
    def kthCharacter(self, k: int) -> str:
        w="a"
        while(len(w)<k):
            r=""
            #print(w)
            for i in range(len(w)):
                if w[i]=='z':
                    r=w+"a"
                else:
                    char=chr(ord(w[i])+1)
                    #print(char)
                    r=r+char
            #print(r)
            w=w+r
        #print(w)
        return w[k-1]