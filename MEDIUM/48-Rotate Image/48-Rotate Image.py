// Problem: Rotate Image
// Difficulty: MEDIUM
// LeetCode URL: https://leetcode.com/problems/rotate-image/
// Date: 2024-07-15

class Solution {
    public void rotate(int[][] a) {
        int t[][]=new int[a.length][a[0].length];
        for(int i=0;i<a.length;i++){
            for(int j=0;j<a.length;j++){
                t[i][j]=a[j][i];
            }
        }
        int n=a.length-1;
        System.out.print(n);
        for(int i=a.length-1;i>=0;i--){
            for(int j=a.length-1;j>=0;j--){
                // System.out.print(t[i][j]+",");
                a[i][n-j]=t[i][j];
            }
        }
    }
}