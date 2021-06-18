# Leetcode -> Easy
# 27. Remove Element
# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums) - nums.count(val)
        for i in range(nums.count(val)):
            nums.remove(val)
        return k

nums = [3, 2, 2, 3]
val = 3