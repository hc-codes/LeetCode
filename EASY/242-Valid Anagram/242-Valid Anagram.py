// Problem: Valid Anagram
// Difficulty: EASY
// LeetCode URL: https://leetcode.com/problems/valid-anagram/
// Date: 2024-08-10

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(s.length()!=t.length()) {return false;}
        int smap[26]={0};
        int tmap[26]={0};
        int len = s.length();
        for(int i=0; i<len; i++) {
            smap[s[i]-97]+=1;
            tmap[t[i]-97]+=1;
        }
        return equal(begin(smap), end(smap), begin(tmap));
    }
};