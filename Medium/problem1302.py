# Leetcode -> Medium
# 1302. Deepest Leaves Sum
# Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
# Output: 15
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 19
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

#Paramater
root = [1,2,3,4,5,null,6,7,null,null,null,null,8]

#Main Function
def main():
    output = Solution()
    print(output.deepestLeavesSum(root))

if __name__ =='__main__':
    main()