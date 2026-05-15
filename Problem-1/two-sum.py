# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return[num_map[complement], i]
            num_map[num] = i


def main():
    s = Solution()

    nums = [2,7,11,15]
    print("Test Case 1")
    print("Expected Value: 9")
    print("Output value: " + str(s.twoSum(nums, 9)))


if __name__ == '__main__':
    main()