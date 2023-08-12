e=0
n=int(input("ENTER THE NO OF EMPLOYEES : "))
o="THE NO OF EMPLOYEES IS : ",n
while e<n:
    e=e+1
    m=int(input("ENTER THE MONTHLY SALARY OF EMPLOYEE "))
    a=m*12
    print("THE ANNUAL SALARY IS :",a)
    if a > 100000:
        print("THIS EMPLOYEE'S SALARY IS MORE THAN 1 LAKHS")
    else:
        print("THIS EMPLOYEE'S SALARY IS LESS THAN 1 LACHS")