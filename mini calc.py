print("WELCOME TO MINI CALCULATOR!!")

i,n=int(input("ENTER THE FIRST VALUE ")),int(input("ENTER THE SECOND VALUE "))
o = int(input("ENTER THE OPERATION YOU NEED,\n1.sum\n2.subtract\n3.division\nmultiplication"))
if o == 1:
    print(i+n)
elif o == 2:
    print(i-n)
elif o ==3:
    print(i//n)
else:
    print(i*n)?