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
        
        s2= s
        s3= s
        
        out=[] 
            
        while len(s3)>0:
                
            minchar = min(s)
            out.append(minchar)
            
            s2= s2.replace(minchar,'',1)
            s=s.replace(minchar,'')
            
            while len(s)>0:
                nextmin = min(s)
                if nextmin > minchar:
                    
                    out.append(nextmin)
                    s=s.replace(nextmin,'')
                    s2= s2.replace(nextmin,'',1)
                    minchar= nextmin
            
            s3=s2
        
        
            if len(s3)>0:
                
                maxchar = max(s2)
                out.append(maxchar)
                s2= s2.replace(maxchar,'')
                s3= s3.replace(maxchar,'',1)
                
                while len(s2)>0:
                    nextmax = max(s2)
                    if nextmax < max(out):
                        out.append(nextmax)
                        s2=s2.replace(nextmax,'')
                        s3=s3.replace(nextmax,'',1)
                        maxchar = nextmax 
                
                s=s3
                s2= s
        
        #step4
        outs=''.join(out)

        return outs
            
a=Solution()
a.sortString("rat")
a.sortString("leetcode")

s='leetcode'