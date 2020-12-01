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

N=23
#8:32
valid = [0,1,8,2,5,6,9]

cnt=0
for i in range(0,N+1):
    sub_cnt=0
    for d in str(i):
        
        if int(d) == 2 or int(d) ==5 or int(d) ==6 or int(d)==9 and int(d) != 3:
        #if int(d) in valid:
            sub_cnt += 1   
            
            
    if sub_cnt >=1: #==len([int(d) for d in str(i)]) :          
        cnt+=1
        print(i,sub_cnt)



class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        


a=Solution()
a.rotatedDigits(N=2)


N=2
for i in range(0,N+1):
    print(i)