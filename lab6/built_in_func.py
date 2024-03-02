#ex1
nums = input()
my_list = [int(x) for x in nums.split()]
sum = sum(my_list)
print(sum)

#ex2
stri=input()
upcount=0
lowcount=0
for i in stri:
    if i.isupper():
        upcount+=1
    elif i.islower():
        lowcount+=1
    else:
        continue   
print(f"lowercase:{lowcount}") 
print(f"uppercase:{upcount}")    

#ex3
def is_palindrome(s):
    s = s.lower()  
    return s == s[::-1]

#ex4
import time
import math

def sqrt_after_mlsc(number, milliseconds):
    time.sleep(milliseconds / 1000) #mili to sec, and code stops for this time
    result = math.sqrt(number)
    return result

num = int(input())
milliseconds = int(input())

result = sqrt_after_mlsc(num, milliseconds):
print(f"Square root of {num} after {milliseconds} milliseconds is {result}")

#ex5
def all_true(t):
    return all(t) #Returns True if all items in an iterable object are true
#example:
tup=(0,1,True) #output is false, coz 0 is false