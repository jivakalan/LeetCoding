# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 13:28:53 2021

@author: kalan
"""
1:31


1641. Count Sorted Vowel Strings
Medium

Given an integer n, return the number of strings of length n that consist only of vowels (a, e, i, o, u) and are lexicographically sorted.

A string s is lexicographically sorted if for all valid i, s[i] is the same as or comes before s[i+1] in the alphabet.

 


Example 1:

Input: n = 1
Output: 5
Explanation: The 5 sorted strings that consist of vowels only are ["a","e","i","o","u"].
Example 2:

Input: n = 2
Output: 15
Explanation: The 15 sorted strings that consist of vowels only are
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
Note that "ea" is not a valid string since 'e' comes after 'a' in the alphabet.


Input: n = 33
Output: 66045

Constraints:

1 <= n <= 50

#add repeats (aaa, aaa,aae)
    
#create all 3 letter combinatoins 






class Solution:
    def countVowelStrings(self, n):
        
        
        from itertools import permutations
        
        #for n = 3
        vowels =['a','e','i','o','u']
        
        perm = permutations(vowels,2)
        out=[]
        for i in list(perm):
            #print(sorted(i) == list(i))
            if sorted(i) == list(i):
                
                out.append(i)
        
        for i in vowels:
            out.append(i+i)
            
        return len(out)