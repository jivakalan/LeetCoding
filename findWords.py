# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 23:55:50 2020

@author: kalan
"""
# =============================================================================
# 
# 500. Keyboard Row
# Easy
# 
# Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


# Example:
# 
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
# =============================================================================
# =============================================================================
 


    

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = 'qwertyuiop'
        row2 = 'asdfghjkl'
        row3 = 'zxcvbnm'
        

        out= []
        
        
        cnt=0
        for word in words:
            for letter in word:
                if letter.lower() in row2:
                    cnt+= 1
            #        print(letter, cnt)
            
            if len(word) == cnt:
                out.append(word)
            cnt =0    
        
        cnt=0
        for word in words:
            for letter in word:
                if letter.lower() in row1:
                    cnt+= 1
             #       print(letter, cnt)
            
            if len(word) == cnt:
                out.append(word)
            cnt =0    
            
            
            
        cnt=0
        for word in words:
            for letter in word:
                if letter.lower() in row3:
                    cnt+= 1
              #      print(letter, cnt)
            
            if len(word) == cnt:
                out.append(word)
            cnt =0
        return out
    
    
    
a=Solution()
a.findWords( words =  ["Hello", "Alaska", "Dad", "Peace"])

        
        #words =['Alaska', 'Dad']