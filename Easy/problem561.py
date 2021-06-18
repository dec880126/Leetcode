# Leetcode  ->  Easy
# Array Partition I
# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.

# Better complement: Runtime = 268 ms ; Memory = 17 MB
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums, reverse = True)
        return sum(nums[i] for i in range(1, len(nums), 2))

# Original complement: Runtime = 296 ms ; Memory = 16.7 MB
# class Solution:
#     def arrayPairSum(self, nums: list[int]) -> int:
#         sum = 0
#         nums.sort()
#         nums = list(list_spilt(nums, 2))
#         for i in range(len(nums)):
#             sum += min(nums[i][0], nums[i][1])
#         return sum

# def list_spilt(list, n):
#     for i in range(0, len(list), n):
#         yield list[i:i+n]

#Paramater
nums = [6,2,6,5,1,2]

#Main Function
def main():
    output = Solution()
    print(output.arrayPairSum(nums))

if __name__ =='__main__':
    main()
