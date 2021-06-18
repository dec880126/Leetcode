# Leetcode -> Easy
# 27. Remove Element
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        for i in range(nums.count(val)):
            nums.remove(val)
        return k

nums = [3, 2, 2, 3]
val = 3
