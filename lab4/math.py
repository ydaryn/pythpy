#ex1
import math
def deg_to_rad(deg):
    rad=deg*math.pi/180
    return rad
n=int(input())
print(deg_to_rad(n))

#ex2
def area_trap(h,fbase, sbase):
    area=((fbase+sbase)*h)/2
    return area
height=int(input())
a=int(input())
b=int(input())
print(area_trap(height,a,b))

#ex3
import math 
def area_poly(n, length):
     return (n * length ** 2) / (4 * math.tan(math.pi / n))
n=int(input())
length=int(input())
print(area_poly(n,length)) 

#ex4
def area_para(b, h):
    return b * h
base=int(input())
height=int(input())
print(area_para(base,height))