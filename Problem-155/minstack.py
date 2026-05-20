# https://leetcode.com/problems/min-stack/description/

class MinStack:

    def __init__(self):
        self.stacklist = []
        self.minstack = []

    
    def push(self, val: int) -> None:
        if not self.minstack or val <= self.minstack[-1]:
            self.minstack.append(val)
        
        self.stacklist.append(val)

    def pop(self) -> None:
        if self.stacklist.pop() == self.minstack[-1]:
            self.minstack.pop()

    def top(self) -> int:
        return self.stacklist[-1] if self.stacklist else 0

    def getMin(self) -> int:
        return self.minstack[-1] if self.minstack else -1
    
    def printStack(self):
        print("[", end="")
        for x in self.stacklist:
            print(x, end=", ")
        
        print("]", end="")
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    obj.printStack()
    obj.pop()
    obj.printStack()
    param_3 = obj.top()
    param_4 = obj.getMin()