# https://leetcode.com/problems/add-two-numbers/?envType=problem-list-v2&envId=r9zp3ka3
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # total[ListNode] = null
        if l1 == None and l2 == None:
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1

        l1_current_node = l1
        l2_current_node = l2
        dummy = ListNode()
        totalList = dummy

        digitSum = 0
        isOverflow = False
        while l1_current_node and l2_current_node:
            
            if(isOverflow):
                digitSum = l1_current_node.val + l2_current_node.val + 1
            else:
                digitSum = l1_current_node.val + l2_current_node.val

            if(digitSum > 9):
                isOverflow = True
                digitSum %= 10
            else:
                isOverflow = False
            
            totalList.next = ListNode(digitSum)
            totalList = totalList.next
            
            l1_current_node = l1_current_node.next
            l2_current_node = l2_current_node.next
        
        while l1_current_node or l2_current_node:
            l1_val = l1_current_node.val if l1_current_node else 0
            l2_val = l2_current_node.val if l2_current_node else 0
            digitSum = l1_val + l2_val + (1 if isOverflow else 0)

            if digitSum > 9:
                isOverflow = True
                digitSum %= 10
            else:
                isOverflow = False

            totalList.next = ListNode(digitSum)
            totalList = totalList.next
            
            l1_current_node = l1_current_node.next if l1_current_node else None
            l2_current_node = l2_current_node.next if l2_current_node else None

        if isOverflow:
            totalList.next = ListNode(1)

        return dummy.next


