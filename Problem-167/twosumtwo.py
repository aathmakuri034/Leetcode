# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Time Complexity: O(n)
# Space Complexity: O(n)
# SOLVED

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if len(numbers) == 2:
            return [1,2] if numbers[0] + numbers[1] == target else []
        
        num_map = {}
        for i, a in enumerate(numbers):
            complement = target - a
            if complement in num_map:
                return [num_map[complement]+1, i+1]
            num_map[a] = i


def main():
    solution = Solution()
    numbers = [2,7,11,15]
    target = 9

    sol = solution.twoSum(numbers=numbers, target=target)
    print(sol)

if __name__ == "__main__":
    main()