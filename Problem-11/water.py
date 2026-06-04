# https://leetcode.com/problems/container-with-most-water/description/
# Time Complexity O(n)
# Space Complexity O(1)
# SOLVED

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        if(len(height) == 2):
            return min(height[0], height[1])
        
        while left < right:
            # Calculate the area from shorter wall
            h = min(height[left], height[right])
            max_area = max(max_area, h * (right - left))

            # Moves the shorter wall
            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1
        
        return max_area


if __name__ == "__main__":
    solution = Solution()

    height1 = [1,8,6,2,5,4,8,3,7]
    print("Expected Output: 49")
    print(f"Actual Output: {solution.maxArea(height1)}\n")
    
    height2 = [1,2]
    print("Expected Output: 1")
    print(f"Actual Output: {solution.maxArea(height2)}\n")
    
    height3 = [1,1]
    print("Expected Output: 1")
    print(f"Actual Output: {solution.maxArea(height3)}\n")