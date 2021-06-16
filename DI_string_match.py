# Input: s = "IDID"
# Output: [0,4,1,3,2]

# Input: s = "III"
# Output: [0,1,2,3]

# Input: s = "DDI"
# Output: [3,2,0,1]

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        least = 0
        most = len(s)
        out = []
        for char in s:
            if char == 'I':
                out.append(least)
                least += 1
            else:
                out.append(most)
                most-=1
        out.append(least)
        return out

#                   Bad complement
# class Solution:
#     def diStringMatch(self, s: str) -> list:
#         string = list(s)
#         #string = ['I', 'D', 'I', 'D']
#         num = [i for i in range(len(string)+1)]
#         #num = [0, 1, 2, 3, 4]
#         output_list = []
#         for i in range(len(string)):
#             if string[i] == "I":
#                 output_list.append(min(num))
#                 del num[num.index(min(num))]
#             elif string[i] == "D":
#                 output_list.append(max(num))
#                 del num[num.index(max(num))]
#             else:
#                 print(f"Type Error for number {i} element in the string")
#         output_list.append(num[0])
#         return output_list
        
#Paramater
s = "DDI"

#Main Function
def main():
    output = Solution()
    print(output.diStringMatch(s))

if __name__ =='__main__':
    main()