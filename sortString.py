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
s="aaaabbbbcccc"

class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        out=[]
        intermed=s
        oldstring = s
        while len(s)>0:        
            intermed = oldstring
            #step 1-3
            
            while len(intermed)>0:
                minchar =min(intermed)
                out.append(minchar)
                intermed= intermed.replace(minchar,'')
                s=s.replace(minchar,'',1)
            
            intermed = oldstring
            
            #step 4-6
            #intermed=s
            if len(s)>0:
                
                while len(intermed)>0:
                    maxchar = max(intermed)
                    out.append(maxchar)
                    intermed= intermed.replace(maxchar,'')
                    s=s.replace(maxchar,'',1)    
        
        #step4
        outs=''.join(out)
        return outs
            
a=Solution()
a.sortString("rat")
a.sortString("leetcode")
