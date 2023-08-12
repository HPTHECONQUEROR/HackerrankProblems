n=int(input('ENTER THE NUMBER OF TERMS : '))
a,b=-1,1
for i in range(1,n+1):
    f = a+b
    fib.append(f)
    a,b = b,f
print(fib,'\n',sum(fib))
