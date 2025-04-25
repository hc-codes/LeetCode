// Problem: Remove Element
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/remove-element/
// Date: 2023-07-30

class Solution {
public:
    int removeElement(vector<int>& arr, int val) {
        int c=0;
        for(int j =0;j<arr.size();j++){
        }  
         for(int j =0;j<arr.size();j++){
        }  
         for(int j =0;j<arr.size();j++){
        }  
        for(int i=0;i<arr.size();i++){
            if(arr[i]!=val){
                arr[c++]=arr[i];
            }
        }

        return c;
    }
};