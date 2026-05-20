# https://leetcode.com/problems/integer-to-roman/description/
# SOLVED - Brute Force
# Time Complexity - O(1)
# Space Complexity - O(1)

class Solution:
    def intToRoman(self, num: int) -> str:
        symList = [
            ["I", 1],
            ["IV", 4],
            ["V", 5],
            ["IX", 9],
            ["X", 10],
            ["XL", 40],
            ["L", 50],
            ["XC", 90],
            ["C", 100],
            ["CD", 400],
            ["D", 500],
            ["CM", 900],
            ["M", 1000]
            ]
        
        numeralList = []
        for sym in reversed(symList):
            print(sym[1])
            val = num // sym[1] # Divides given value buy second element in symList and rounds down
            numeralList.append(sym[0] * val if val > 0 else "")
            num %= sym[1] # Gives me what is left after roman number is added
            val = 0
        
        return "".join(numeralList)



if __name__ == "__main__":
    s = Solution()

    print("Test Case 1")
    print("Expected Output: MMMDCCXLIX")
    print("Actual Output: " + s.intToRoman(3749))
    print("=" * 30)
