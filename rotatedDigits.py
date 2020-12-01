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


valid =[0,1,8,2,5,6,9]

rotate = [2,5,6,9]
invalid =[3,4,7]
x is a good number if, after rotation, we get a valid number that is different from X 

230
5(rotate),3(invalid),(0)valid, not valid! 
596
2-6,9 all rotated, valid
536 
2-invalid-9, invalid


N=10
cnt=0

for number in range(0,N+1):
    for digit in str(number):
        if int(digit) in valid:
            print(number, 'yes')
        else:
            break
    cnt+=1

    

class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        #NEW SOLUTION


a=Solution()
a.rotatedDigits(N=857)

