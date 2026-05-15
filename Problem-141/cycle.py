# https://leetcode.com/problems/linked-list-cycle/description/
#SOLVED

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        s = set()
        temp = head

        while temp:
            if temp in s:
                return True
            else:
                s.add(temp)
            temp = temp.next
        
        return False
    

if __name__ == "__main__":
    s = Solution()
