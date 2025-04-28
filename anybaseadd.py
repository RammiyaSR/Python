from math import log
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def AnyBaseAddition(A, B, C):
        carry = 0
        ans = 0
        power = 1
        while B>0 or C>0 or carry>0:
            digit1 = B % 10
            digit2 = C % 10
            dig = digit1 + digit2 + carry
            carry = dig // A
            dig = dig % A
            ans = ans +dig*power
            power *= 10
            B = B // 10
            C = C //10
        return ans

obj = Solution
print("Enter the base:")
a= int(input())
print("Enter the first no:")
b= int(input())
print("Enter the second no:")
c= int(input())
print("Result:",obj.AnyBaseAddition(a,b,c))