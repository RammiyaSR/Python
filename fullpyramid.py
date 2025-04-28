#     *
#    * *
#   * * *
#  * * * *
# * * * * *
print("Enter the size of the pyramid:")
N = int(input())
for i in range(1,N+1):
    print(" " * (N-i),end="")
    print("* " * i,end="")
    print()