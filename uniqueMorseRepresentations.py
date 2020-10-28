# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 22:45:37 2020

@author: kalan
"""

# =============================================================================
# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example, "cab" can be written as "-.-..--...", (which is the concatenation "-.-." + ".-" + "-..."). We'll call such a concatenation, the transformation of a word.
# 
# Return the number of different transformations among all words we have.
# 
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation: 
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
# =============================================================================

#There are 2 different transformations, "--...-." and "--...--.".

10:47


morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

import string

alphabet={}
c=0
for i in string.ascii_lowercase:
    
    alphabet[c]=i
    c+=1

alphabet_to_morse = {}    
for i in range(len(alphabet)):
    alphabet_to_morse[alphabet[i]] = morse[i]
    

words = ["gin"]

translation={}
for word in words:
    translation=[]
    for letter in word:
        
        print(letter,alphabet_to_morse[letter])
        
