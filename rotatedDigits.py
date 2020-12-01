# =============================================================================
# 788. Rotated Digits
# 
# X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
# 
# A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
# 
# Now given a positive number N, how many numbers X from 1 to N are good?
# 
# Example:
# Input: 10
# Output: 4
# Explanation: 
# There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
# Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.
# =============================================================================

N=857
#8:32
N=10


    

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        #NEW SOLUTION
        dic={'0':'0','1':'1', '2':'5','3':'3', '4':'4', '5':'2','6':'9', '7':'7', '8':'8', '9':'6'}

        cnt=0
        for i in range(0,N+1):
           # print(i)  
            out=''      
            for digit in str(i):
             #   print(digit)
                out = out + dic[digit]
            
            if int(out)!=i:
                cnt+=1
        return cnt

a=Solution()
a.rotatedDigits(N=857)

