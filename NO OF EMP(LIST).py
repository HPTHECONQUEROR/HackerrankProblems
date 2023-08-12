n=int(input("ENTER THE NUMBER OF EMPLOYEES : "))
sal=[]
for i in range(1,n+1):
  sal.append(int(input(f'ENTER THE SALARY OF {i} : ',)))
lak=[]
for i in sal:
    if (i*12>=100000):
        lak.append(i)
print('THE NO OF EMPLOYEES OUT OF ',n,'IS',len(lak))