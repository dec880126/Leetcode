# Leetcode  ->  Medium
# Minimum Number of Operations to Move All Balls to Each Box
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, 
# and move one ball from the second box to the third box in one operation.

# Better implementation: Runtime =  68 ms ; Memory =  14.4 MB
class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        if len(boxes) == 1:
            return [0]
        idx = set() # set of i for which boxes[i] == '1'
        tot = 0     # sum of items in idx
        for i, b in enumerate(boxes):
            if b == '1':
                idx.add(i)
                tot += i
        r = len(idx)    # running number of 1s right of index i
        l = 0           # running number of 1s left of index i
        out = [tot]
        for i in range(1, len(boxes)):
            if i-1 in idx:
                r -= 1
                l += 1
            tot += -r + l
            out.append(tot)
        return out

# Original implementation: Runtime =  5360 ms ; Memory =  14.6 MB
# class Solution:
#     def minOperations(self, boxes: str) -> list[int]:
#         box_list = list(boxes)  #[0, 0, 1, 0, 1, 1]
#         step_list = []
#         n = len(box_list)
#         for i in range(n):
#             step = 0
#             for j in range(n):                
#                 if box_list[j] == '1':
#                     step += abs(j - i)
#             step_list.append(step)
#         return step_list


#Paramater
boxes = "001011"
# Output: [11,8,5,4,3,4]

#Main Function
def main():
    output = Solution()
    print(list(boxes))
    print(output.minOperations(boxes))

if __name__ =='__main__':
    main()
