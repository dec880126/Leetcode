# Leetcode  ->  Easy
# Height Checker
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.

# Original complement: Runtime = 32 ms ; Memory = 14.1 MB
class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        excepted = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != excepted[i]:
                count += 1
        return count 


#Paramater
heights = [1,2,3,4,5]

#Main Function
def main():
    output = Solution()
    print(output.heightChecker(heights))

if __name__ =='__main__':
    main()