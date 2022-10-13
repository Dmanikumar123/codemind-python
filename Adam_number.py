n=int(input())
s=n**2
p=0
while n>0:
    r=n%10
    p=p*10+r
    n=n//10
sp=p**2
rsp=0
while sp>0:
    q=sp%10
    rsp=rsp*10+q
    sp=sp//10
if s==rsp:
    print(True)
else:
    print(False)