Given two strings as input, find number of occurrences of last character in second string, in the first string. Don't use string library functions for this program

Input: “going to go to goa”, “go”
Output: 5 (last char of str2 is o and it appeared 5 times in str1)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------

string1=input()
string2=input()
last_chr=string2[-1]
count=0
for i in string1:
    if i==last_chr:
        count+=1
print(count)
