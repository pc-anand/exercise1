a=2
b=5
c=a+b
print(c)
d=a*b
e=a/b
f=b-a
print(d)
print(e)
print(f)
# simple intrest
p=float(input("enter principal amount"))
r=float(input("enter rate of intrest"))
t=float(input("enter time period"))
SI=(p*r*t)/100
print("simple intrest is", SI)
# swapping using third variable
a=int(input("enter a"))
b=int(input("enter b"))
c=a
a=b
b=c
print(a)
print(b)
#swapping without using third variable
a=int(input("enter a"))
b=int(input("enter b"))
a=a+b
b=a-b
a=a-b
print(a)
print(b)
# circumference of a circle
r=int(input("enter the value radius"))
pi=3.14
circumference=(2*pi*r)
print(circumference)
# area of circle
pi=3.14
r=int(input("enter the value of radius "))
area=pi*r**2
print(area)
# height from feet to inches
h=float(input("enter the height in feets"))
height_in_inches=12*h
height_in_cm=height_in_inches*2.54
print(height_in_inches)
print(height_in_cm)
# reversal of three digit numbers
num=int(input("enter the three digit number"))
a=num%10
num=num//10
b=num%10
num=num//10
c=num%10
print("reverse of the number id",a*100+b*10+c)
# conversion of temprature
T=float(input("enter the temprature in degree"))
f=1.8*T+240
print(f)
# calculation of gross salary
basic_salary=float(input("enter the amount"))
HRA=(basic_salary*30)/100
TA=(basic_salary*40)/100
DA=(basic_salary*20)/100
gross_salary=basic_salary+HRA+TA+DA
print("\n TA",TA)
print("HRA",HRA)
print("DA",DA)
print("gross salary:",gross_salary)