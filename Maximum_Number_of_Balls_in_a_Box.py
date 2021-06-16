# Leetcode  ->  Easy
# Maximum Number of Balls in a Box
# Input: lowLimit = 5, highLimit = 15
# Output: 2
# Explanation:
# Box Number:  1 2 3 4 5 6 7 8 9 10 11 ...
# Ball Count:  1 1 1 1 2 2 1 1 1 0  0  ...
# Boxes 5 and 6 have the most number of balls with 2 balls in each.

# Better complement: Runtime = 672 ms ; Memory = 14.3 MB
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        dic = {}
        for i in range(lowLimit, highLimit+1):
            digit_sum = sum(map(int, list(str(i))))
            if digit_sum not in dic.keys():
                dic[digit_sum] = 1
            else:
                dic[digit_sum] += 1
        return max(dic.values())

# Bad complement: Runtime = 1072 ms ; Memory = 14.3 MB
# class Solution:
#     def countBalls(self, lowLimit: int, highLimit: int) -> int:
#         n = highLimit - lowLimit + 1
#         box = []
#         for i in range(lowLimit, highLimit+1):
#             digit = [int(x) for x in str(i)]
#             sum = 0
#             for j in digit:
#                 sum += int(j)
#             while (len(box)+1) < sum+1:
#                 box.append(0)
#             box[sum-1] += 1
#         return max(box)


#Paramater
lowLimit = 19
highLimit = 28

#Main Function
def main():
    output = Solution()
    print(output.countBalls(lowLimit, highLimit))

if __name__ =='__main__':
    main()