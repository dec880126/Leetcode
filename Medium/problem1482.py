# Leetcode -> Medium
# 1482. Minimum Number of Days to Make m Bouquets
# Input: bloomDay = [1,10,3,10,2], m = 3, k = 1
# Output: 3
# Explanation: Let's see what happened in the first three days. x means flower bloomed and _ means flower didn't bloom in the garden.
# We need 3 bouquets each should contain 1 flower.
# After day 1: [x, _, _, _, _]   // we can only make one bouquet.
# After day 2: [x, _, _, _, x]   // we can only make two bouquets.
# After day 3: [x, _, x, _, x]   // we can make 3 bouquets. The answer is 3.

# Input: bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
# Output: 9



class Solution:
    def minDays(self, bloomDay, m, k):
        """
        type bloomDay: list[int]
        type m: int
        type k: int
        rtype: int
        """
        N = len(bloomDay)
        if N < m*k:
            return -1
        start = min(bloomDay)
        end = max(bloomDay)
        res = 0
        while start <= end:
            mid = start + (end - start)//2
            if self.isValid(N, bloomDay, m, k, mid):
                res = mid
                end = mid - 1
            else:
                start = mid + 1
        return res

    def isValid(self, N, bloomDay, m, k, mid):
        stack = []
        bouquets = 0
        i = 0
        while i < N:
            if len(stack) == k:
                bouquets += 1
                stack = []
            if bloomDay[i] <= mid:
                stack.append(bloomDay[i])
            else:
                stack = []
            i += 1
        if len(stack) == k:
            bouquets += 1
        if bouquets < m:
            return False
        return True
      
bloomDay = [1,10,2,9,3,8,4,7,5,6]
m = 4
k = 2

output = Solution()
print(output.minDays(bloomDay, m, k))
