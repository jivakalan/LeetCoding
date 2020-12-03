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


class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        selves = [0,1,8]
        rotate = [2,5,6,9]
        invalid =[3,4,7]

        cnt=0
        out=[]
        for i in range(0,N+1):
            
            sub_cnt=0
            for digit in str(i):
                
                if int(digit) in rotate :
                    sub_cnt+=1
                if int(digit) in invalid:
                    sub_cnt = sub_cnt - 1
                    #print(i, sub_cnt)
            
           
            
            if sub_cnt >= 1:
                cnt+=1
                #print(i,sub_cnt)
                out.append(i)
            
        for num in out:
            for digit in str(num):
                
                if int(digit) in invalid :
                    cnt = cnt - 1        
        return cnt

a=Solution()
a.rotatedDigits(N=10)

