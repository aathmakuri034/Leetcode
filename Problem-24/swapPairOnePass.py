# https://leetcode.com/problems/swap-nodes-in-pairs/description/
# Time Complexity: O(n)
# Space Complexity: O(1)
# SOLVED

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        if head.next is None:
            return head
        
        dummy = ListNode(0, head)
        prev_node = dummy
        curr_node = head

        while curr_node and curr_node.next:
            first = curr_node
            second = curr_node.next

            prev_node.next = second
            first.next = second.next
            second.next = first

            prev_node = first
            curr_node = first.next
            
        return dummy.next


def build_linked_list(values: list[int]) -> Optional[ListNode]:
    dummy = ListNode(0)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
    result: list[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    values = [1, 2, 3, 4]
    head = build_linked_list(values)
    result_head = Solution().swapPairs(head)
    print("Input:", values)
    print("Output:", linked_list_to_list(result_head))
    


    
