"""
In this section we will see about flow control of python , first we see if elif,and then we move onwards to range
function.
____________________________________________________________________________________________________________________
Question : Write a function based on if elif and range function.
________________________________________________________________
Approach : First take input from user and then compare it by use of if elif and then print that number in order of
           lower to the highest by using range function.
"""
A = int(input("Enter the number : "))
if A < 10:
    print("Number will execute")
elif A < 9:
    print("number is odd :")
elif A < 8:
    print("number is even :")
else:
    print("Number is not correct :")

B = "python is programming language "
print(B)

C = int(input("Enter the second number : "))
if C < 20:
 for C in range(C, 20, 2):
    print(C, end=',')
else:
    print("Invalid number enter by user : ")
