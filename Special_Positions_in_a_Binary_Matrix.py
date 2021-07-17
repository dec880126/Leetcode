# Leetcode  ->  Easy
# Special Positions in a Binary Matrix
# Input: mat = [[0,0,0,0,0],
#               [1,0,0,0,0],
#               [0,1,0,0,0],
#               [0,0,1,0,0],
#               [0,0,0,1,1]]
# Output: 3

# Original complement: Runtime = 296 ms ; Memory = 16.7 MB
class Solution:
    def numSpecial(self, mat: list[list[int]]) -> int:
        
#Paramater
mat = [[0,0,0,0,0],
       [1,0,0,0,0],
       [0,1,0,0,0],
       [0,0,1,0,0],
       [0,0,0,1,1]]

#Main Function
def main():
    output = Solution()
    print(output.numSpecial(mat))

if __name__ =='__main__':
    main()