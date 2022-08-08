#Write a program to calculate the average of all even integers between one and ten thousand 

sum=0
count=0
for y in range(1,10000):
    if int(y%2)==0:
        count=count+1
        sum=sum+y
average=sum/count
print("The average is",average)

