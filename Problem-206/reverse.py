# https://leetcode.com/problems/reverse-linked-list/
# Solved

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reversedList(self, head: ListNode) -> ListNode:
        prev_node = None
        curr_node = head

        while(curr_node):
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
        
        return prev_node
    

def print_list(head):
    """Helper function to print the linked list."""
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

if __name__ == "__main__":
    # Example 1: head = [1,2,3,4,5]
    # Create the list: 1 -> 2 -> 3 -> 4 -> 5 -> None
    node5 = ListNode(5)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head_example1 = ListNode(1, node2)

    print("Original List 1:")
    print_list(head_example1)

    solver = Solution()
    reversed_head1 = solver.reversedList(head_example1)

    print("Reversed List 1:")
    print_list(reversed_head1)
    # Expected output: 5 -> 4 -> 3 -> 2 -> 1 -> None
    print("-" * 20)

    # Example 2: head = [1,2]
    # Create the list: 1 -> 2 -> None
    head_example2 = ListNode(1, ListNode(2))
    print("Original List 2:")
    print_list(head_example2)

    reversed_head2 = solver.reversedList(head_example2)
    print("Reversed List 2:")
    print_list(reversed_head2)
    # Expected output: 2 -> 1 -> None