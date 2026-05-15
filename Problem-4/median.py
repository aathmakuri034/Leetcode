# https://leetcode.com/problems/median-of-two-sorted-arrays/description/
# Solved
class Solution:
    def findMedianOfTwoArrays(self, nums1: list, nums2: list ) -> int:
        nums1.extend(nums2)
        nums1 = sorted(nums1)

        n = len(nums1)

        if(n%2 == 0):
            median = (nums1[int(n/2)] + nums1[int(n/2) - 1]) / 2
        else:
            median = nums1[n//2]

        return median

if __name__ == "__main__":
    s = Solution()
    print("Test Case 1")
    nums1 = [1,2]
    nums2 = [3]
    print("Expected Value: 2")
    print("Output Value: " + str(s.findMedianOfTwoArrays(nums1, nums2)))

    print("Test Case 2")
    nums1 = [1,2]
    nums2 = [3,4]
    print("Expected Value: 2.50000")
    print("Output Value: " + str(s.findMedianOfTwoArrays(nums1, nums2)))

