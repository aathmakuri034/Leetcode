# https://leetcode.com/problems/product-of-array-except-self/description/
# Not Solved
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
       n = len(nums)
       answer = [0] * n

       prefix_answer = 1
       postfix_answer = 1

       
       
       return answer


if __name__ == "__init__":
    s = Solution()

    nums = [1,2,3,4]
    print("Test Case 1")
    print("Nums: " + str(nums))
    print("Expected Output: [24,12,8,6]")
    print("Actual Output: " + str(s.productExceptSelf(nums)))
    print("Test Case Passed") if s.productExceptSelf(nums) == [24,12,8,6] else print("Test Case Failed")

    nums = [-1,1,0,-3,3]
    print("Test Case 2")
    print("Nums: " + str(nums))
    print("Expected Output: [0,0,9,0,0]")
    print("Actual Output: " + str(s.productExceptSelf(nums)))

