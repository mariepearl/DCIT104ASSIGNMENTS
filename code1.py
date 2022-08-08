#Write a program that produces the sum of all prime numbers less than a given number

from tkinter import X


input=int(input("Enter a prime number"))
sum=0
for num in range(2,input+1):
    X=2
    for x in range(2,num):
        if(int(num%x)==0):
           x=num
           break;
    if x is not num:
        sum+=num
print("The sum of prime numbers up to",input,"is",sum)