def f(n):
   return 1 if (n==1 or n==0) else n * f ( n - 1 )
n=int(input())
print(f(n))
''''n=int(input())
m=n
for i in range(1,n):
   b=m*i
   m=b
print(b)'''