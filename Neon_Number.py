x=int(input())
n=x**2
sum=0
while n!=0:
    r=n%10
    sum=sum+r
    n=n//10
if sum==x:
    print("Neon Number")
else:
    print("Not Neon Number")