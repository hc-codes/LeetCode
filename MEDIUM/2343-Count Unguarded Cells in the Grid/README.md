# Count Unguarded Cells in the Grid

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/count-unguarded-cells-in-the-grid/](https://leetcode.com/problems/count-unguarded-cells-in-the-grid/)

---

# Count Unguarded Cells in the Grid

**Difficulty**: Medium

**Tags**: Array, Matrix, Simulation

---

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

&nbsp;
Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.


Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.


&nbsp;
Constraints:


	1 &lt;= m, n &lt;= 105
	2 &lt;= m * n &lt;= 105
	1 &lt;= guards.length, walls.length &lt;= 5 * 104
	2 &lt;= guards.length + walls.length &lt;= m * n
	guards[i].length == walls[j].length == 2
	0 &lt;= rowi, rowj &lt; m
	0 &lt;= coli, colj &lt; n
	All the positions in guards and walls are unique.



