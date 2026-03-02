# 19 - Minimum Window Substring

**Difficulty:** Hard | **Link:** https://neetcode.io/problems/minimum-window-with-characters/question

## 1. Problem Description
```text
Given two strings s and t, return the shortest substring of s such that every character in t,
including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
```

**Example 1:**
```text
Input: s = "OUZODYXAZV", t = "XYZ"

Output: "YXAZ"

Explanation: "YXAZ" is the shortest substring that includes "X", "Y", and "Z" from string t.
```

**Example 2:**
```text
Input: s = "xyz", t = "xyz"

Output: "xyz"
```

**Example 3:**
```text
Input: s = "x", t = "xy"

Output: ""
```

**Constraints:**
```text
1 <= s.length <= 1000
1 <= t.length <= 1000
s and t consist of uppercase and lowercase English letters.
```

## 2. My Approach
```text
This is clearly a sliding window problem. The word "window" is literally in the problem name.
Okay, but in actuality, this problem involves identifying substrings that satisfy a given
condition which is perfect for the sliding window pattern.

If you were to brute force this problem, you'd just check every possible substring possible
and keep track of the shortest one that meets the condition. This algorithm would have
a time complexity of O(n^2) which is pretty slow. Thus, we use sliding window to eliminate
the rechecking of already unqualified substrings.

This problem is pretty similar to some other sliding window problems I've done, like the
one where you check whether or not any substring in a string is a permutation of another
string. 

The catch: this problem is different because the substring can have characters that t
doesn't have, but can still be valid. The only characters you care about are the ones 
that are in string t. Thus, when comparing the two frequency maps, only check the chars
that appear in t.
Also, characters are case sensitive.

How do we validate the substrings and know when to shrink or expand it? We just
keep expanding the window through the right pointer until we hit a valid substring
that satisfies the condition. Then, we want the shortest possible one, so we shrink
it from the left until we get the shortest substring that's still valid. Then, we 
compare it to the previously found minimum-length substring.

Edge cases: 
1. If t is longer than s or an empty string, return an empty string immediately.

Actual implementation (python):
- If len(t) > len(s) return ""
- Initialize freq_t, window for t char frequencies and substr char frequencies.
- l = 0 for the left side of the window.
- Initialize min_string = "" variable.
- min_len = float('infinity')
- make a helper function is_valid to check the validity of a substring:
for char, count in freq_t.items(): 
if window.get(char, 0) < count: return False
else: return True
- for r in range(len(s)) for the right side of the dynamic window.
- char = s[r]
- window[char] = window.get(s[r], 0) + 1
- while is_valid:
	- if the length of the valid substring < the min_len found so far,
	make it our new min_string.
	- pop left character
- Extract the indices and return the resulting min_string.
```

