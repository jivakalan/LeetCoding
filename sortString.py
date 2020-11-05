# =============================================================================
# Given a string s. You should re-order the string using the following algorithm:
# 
# Pick the smallest character from s and append it to the result.
# Pick the smallest character from s which is greater than the last appended character to the result and append it.
# Repeat step 2 until you cannot pick more characters.
# Pick the largest character from s and append it to the result.
# Pick the largest character from s which is smaller than the last appended character to the result and append it.
# Repeat step 5 until you cannot pick more characters.
# Repeat the steps from 1 to 6 until you pick all characters from s.
# In each step, If the smallest or the largest character appears more than once you can choose any occurrence and append it to the result.
# 
# Return the result string after sorting s with this algorithm.
# =============================================================================


s = "aaaabbbbcccc"
output = "abccbaabccba"

result = list(i for i in s)

result2 = []

#step 1
out=[]
intermed=""
for i in range(0,len(s)):
    ##inte=i
    
    print(s[i],i, intermed< s[i])
    if intermed < s[i] :
        out.append(s[i])
    else:
        continue 
    intermed = s[i]
                
#step 2
intermed=''

result.sort(reverse = True)

for i in range(0,len(s)):
        
    if intermed > s[i] :        
        
        print('continue')

    else:
        out.append(s[i]) 
        
    intermed = s[i]
                


#step 3


class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        