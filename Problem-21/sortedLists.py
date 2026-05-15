# https://leetcode.com/problems/merge-two-sorted-lists/description/
# DONE

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

        mergedList = ListNode()
        current = mergedList
        
        while list1 and list2:
            if(list1.val < list2.val):
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            
            current = current.next
        
        # This handles the case where one list is larger than the other list. Adds the remaining node from the longer list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return mergedList.next
        
# --- HELPER FUNCTIONS FOR VS CODE ---
def print_linked_list(node: Optional[ListNode]):
    """Helper function to print the linked list nicely in the terminal."""
    if not node:
        print("[]")
        return
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

def create_linked_list(arr: list) -> Optional[ListNode]:
    """Helper function to convert a normal Python list to a Linked List."""
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# --- LOCAL TESTING SETUP ---
if __name__ == "__main__":
    # Your three test cases
    test_cases = [
        ([1, 2, 4], [1, 3, 4]), # Example 1
        ([], []),               # Example 2
        ([], [0])               # Example 3
    ]
    
    sol = Solution()
    
    for i, (arr1, arr2) in enumerate(test_cases):
        print(f"\n--- Test Case {i+1} ---")
        
        # 1. Build the linked lists from the arrays
        list1 = create_linked_list(arr1)
        list2 = create_linked_list(arr2)
        
        print("Input list1:", end=" ")
        print_linked_list(list1)
        print("Input list2:", end=" ")
        print_linked_list(list2)
        
        # 2. Run your solution
        merged_head = sol.mergeTwoLists(list1, list2)
        
        # 3. Print the results
        print("Output:     ", end=" ")
        print_linked_list(merged_head)