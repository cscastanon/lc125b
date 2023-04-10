#Leetcode # 125 | Valid Palindrome
#My solution: 4/10/2023
#Problem Difficulty Level: Easy
#Solution 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        
        return newStr == newStr[::-1]