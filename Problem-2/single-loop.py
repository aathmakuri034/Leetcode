# https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=r9zp3ka3
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            digitSum = l1_val + l2_val + carry

            digit = digitSum % 10
            carry = digitSum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result
    

# ------------------RUNNER CODE ONLY------------------
def list_to_array(node: Optional[ListNode]) -> list:
    """Convert linked list to array for easy printing"""
    result = []
    current = node
    while current:
        result.append(current.val)
        current = current.next
    return result


def array_to_list(arr: list) -> Optional[ListNode]:
    """Convert array to linked list"""
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def test_add_two_numbers():
    """Test cases for Add Two Numbers"""
    solution = Solution()

    # Test 1: 342 + 465 = 807
    # Represented as [2,4,3] + [5,6,4]
    print("=" * 50)
    print("Test 1: 342 + 465 = 807")
    l1_arr = [2, 4, 3]
    l2_arr = [5, 6, 4]
    l1 = array_to_list(l1_arr)
    l2 = array_to_list(l2_arr)
    result = solution.addTwoNumbers(l1, l2)
    result_arr = list_to_array(result)
    expected = [7, 0, 8]
    print(f"  Input 1: {l1_arr}")
    print(f"  Input 2: {l2_arr}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result_arr}")
    print(f"  Status: {'✅ PASS' if result_arr == expected else '❌ FAIL'}")
    assert result_arr == expected, f"Test 1 failed: expected {expected}, got {result_arr}"

    # Test 2: 0 + 0 = 0
    print("=" * 50)
    print("Test 2: 0 + 0 = 0")
    l1_arr = [0]
    l2_arr = [0]
    l1 = array_to_list(l1_arr)
    l2 = array_to_list(l2_arr)
    result = solution.addTwoNumbers(l1, l2)
    result_arr = list_to_array(result)
    expected = [0]
    print(f"  Input 1: {l1_arr}")
    print(f"  Input 2: {l2_arr}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result_arr}")
    print(f"  Status: {'✅ PASS' if result_arr == expected else '❌ FAIL'}")
    assert result_arr == expected, f"Test 2 failed: expected {expected}, got {result_arr}"

    # Test 3: 9999999 + 9999 = 10009998
    # Represented as [9,9,9,9,9,9,9] + [9,9,9,9]
    print("=" * 50)
    print("Test 3: 9999999 + 9999 = 10009998")
    l1_arr = [9, 9, 9, 9, 9, 9, 9]
    l2_arr = [9, 9, 9, 9]
    l1 = array_to_list(l1_arr)
    l2 = array_to_list(l2_arr)
    result = solution.addTwoNumbers(l1, l2)
    result_arr = list_to_array(result)
    expected = [8, 9, 9, 9, 0, 0, 0, 1]
    print(f"  Input 1: {l1_arr}")
    print(f"  Input 2: {l2_arr}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result_arr}")
    print(f"  Status: {'✅ PASS' if result_arr == expected else '❌ FAIL'}")
    assert result_arr == expected, f"Test 3 failed: expected {expected}, got {result_arr}"

    # Test 4: Different lengths
    print("=" * 50)
    print("Test 4: 99 + 1 = 100")
    l1_arr = [9, 9]
    l2_arr = [1]
    l1 = array_to_list(l1_arr)
    l2 = array_to_list(l2_arr)
    result = solution.addTwoNumbers(l1, l2)
    result_arr = list_to_array(result)
    expected = [0, 0, 1]
    print(f"  Input 1: {l1_arr}")
    print(f"  Input 2: {l2_arr}")
    print(f"  Expected: {expected}")
    print(f"  Got:      {result_arr}")
    print(f"  Status: {'✅ PASS' if result_arr == expected else '❌ FAIL'}")
    assert result_arr == expected, f"Test 4 failed: expected {expected}, got {result_arr}"

    print("=" * 50)
    print("✅ All tests passed!")


if __name__ == "__main__":
    test_add_two_numbers()



