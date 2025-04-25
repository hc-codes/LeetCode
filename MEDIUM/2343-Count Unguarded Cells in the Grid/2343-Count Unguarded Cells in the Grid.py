// Problem: Count Unguarded Cells in the Grid
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/
// Date: 2024-11-21

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        arr= [["x" for j in range(n)] for i in range(m)]
        c = 0
        # print(m,n)
        for i in guards:
            k,j = i[0],i[1]
            # print(i)
            arr[k][j] = 'G'
        for w in walls:
            i, j = w[0], w[1]
            arr[i][j] = 'W'
        gw=set()
        gw.add("W")
        gw.add("G")
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 'G':
                    # up 
                    up, down = i-1, i+1
                    left, right = j-1, j+1
                    while up>=0 and arr[up][j] not in gw:
                        if arr[up][j] != "-":
                            c += 1
                        arr[up][j] = "-"
                        up -= 1
                    # down
                    while (down < len(arr)) and arr[down][j] not in gw:
                        # print(arr[down][j])
                        if arr[down][j] != "-":
                            c += 1
                        arr[down][j] = "-"
                        down += 1
                        # print(down, j, end="->")
                    
                    # left
                    while left >= 0 and arr[i][left] not in gw:
                        if arr[i][left] != "-":
                            c += 1
                        arr[i][left] = "-"
                        left -= 1
                    
                    # right
                    while right < n and arr[i][right] not in gw:
                        if arr[i][right] != "-":
                            c += 1
                        arr[i][right] = "-"
                        right += 1
        # for i in range(m):
        #     for j in range(n):
        #         print(arr[i][j], end=" ")
        #     print()
        # print(m, n, len(guards), len(walls), c)
        return (m * n) - (len(guards) + len(walls) + c)