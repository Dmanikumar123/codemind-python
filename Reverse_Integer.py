n=int(input())
a=abs(n)
s=str(a)
m=s[::-1]
mm=int(m)
if n<0:
    print(-mm)
else:
    print(mm)