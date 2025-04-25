# Sentence Similarity III

**Difficulty**: MEDIUM

**URL**: [https://leetcode.com/problems/sentence-similarity-iii/](https://leetcode.com/problems/sentence-similarity-iii/)

---

# Sentence Similarity III

**Difficulty**: Medium

**Tags**: Array, Two Pointers, String

---

You are given two strings sentence1 and sentence2, each representing a sentence composed of words. A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert an arbitrary sentence (possibly empty) inside one of these sentences such that the two sentences become equal. Note that the inserted sentence must be separated from existing words by spaces.

For example,


	s1 = &quot;Hello Jane&quot; and s2 = &quot;Hello my name is Jane&quot; can be made equal by inserting &quot;my name is&quot; between &quot;Hello&quot; and &quot;Jane&quot; in s1.
	s1 = &quot;Frog cool&quot; and s2 = &quot;Frogs are cool&quot; are not similar, since although there is a sentence &quot;s are&quot; inserted into s1, it is not separated from &quot;Frog&quot; by a space.


Given two sentences sentence1 and sentence2, return true if sentence1 and sentence2 are similar. Otherwise, return false.

&nbsp;
Example 1:


Input: sentence1 = &quot;My name is Haley&quot;, sentence2 = &quot;My Haley&quot;

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting &quot;name is&quot; between &quot;My&quot; and &quot;Haley&quot;.


Example 2:


Input: sentence1 = &quot;of&quot;, sentence2 = &quot;A lot of words&quot;

Output: false

Explanation:

No single sentence can be inserted inside one of the sentences to make it equal to the other.


Example 3:


Input: sentence1 = &quot;Eating right now&quot;, sentence2 = &quot;Eating&quot;

Output: true

Explanation:

sentence2 can be turned to sentence1 by inserting &quot;right now&quot; at the end of the sentence.


&nbsp;
Constraints:


	1 &lt;= sentence1.length, sentence2.length &lt;= 100
	sentence1 and sentence2 consist of lowercase and uppercase English letters and spaces.
	The words in sentence1 and sentence2 are separated by a single space.



