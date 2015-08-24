# coding=utf-8
import sys
__author__ = 'Administrator'
x=0
sum1=0
#for x会自动+1
for x in range(100):
    sum1=x+sum1
print sum1
#while x需要自己加1
x=0
sum2=0
while x in range(100):
    sum2=x+sum2
    x=x+1
print sum2
def addnum(a,b):
    sum=0
    while a<=b:
     sum=a+sum
     a=a+1
    return sum

print addnum(0,5)

print addnum(int(sys.argv[1]),int(sys.argv[2]))

