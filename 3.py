An LCD (Liquid Crystal Display) can represent multiple digits between 0 to 9 
If you turn the LCD upside-down, some of the numbers still remain valid numbers. For example, 16 becomes 91, 10 becomes 01, which are valid numbers.
If you index all positive numbers (>0) that can produce valid numbers when you upside down the display (like 1st one is 1, 2nd one is 2, 3rd one 5... 7th one is 10), 
Write program to print the ’Nth’ number in the series

Input: 8
Output: 11
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

def upsidedown(string) :
    for i in range(len(string)) :
        if (string[i] == '3' or string[i] == '4') :
            return False
    return True

n=int(input())
count=0
i=1
while n!=count:
    if upsidedown(str(i)):
        count+=1
    i+=1
print(i)
