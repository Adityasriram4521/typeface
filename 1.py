Given an integer as input. Write a function to convert that to base 3 number

Input: 10 
Output: 101
-------------------------------------------------------------------------------------------

num=int(input())
res=''
while num>0:
    res=str(num%3)+res
    num=num//3
print(res)
