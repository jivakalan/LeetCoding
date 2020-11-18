
# =============================================================================
# 657. Robot Return to Origin
# There is a robot starting at position (0, 0), the origin, on a 2D plane. Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.
# 
# The move sequence is represented by a string, and the character moves[i] represents its ith move. Valid moves are R (right), L (left), U (up), and D (down). If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.
# 
# Note: The way that the robot is "facing" is irrelevant. "R" will always make the robot move to the right once, "L" will always make it move left, etc. Also, assume that the magnitude of the robot's movement is the same for each move.
#  
# Example 1:
# 
# Input: moves = "UD"
# Output: true
#
#Example 2:
#Input: moves = "LL"
#Output: false
# =============================================================================

    #10:20
    #10:26-accepted/submitted
 


        
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        
        x_axis = 0
        y_axis = 0
        for letter in moves:
            if letter =='U':
                x_axis += 1
            if letter =='D':
                x_axis = x_axis - 1
            
            if letter =='R':
                y_axis += 1
            if letter =='L':
                y_axis = y_axis - 1
            
        if x_axis == 0 and y_axis ==0:
            return True
        else: 
            return False

a=Solution()
a.judgeCircle(moves ="LL")


