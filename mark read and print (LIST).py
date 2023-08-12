f=['TAMIL','ENGLISH','MATHS','PHYSICS','CHEMISTRY','COMPUTER SCIENCE']
ma=[]
for t in f:
   m = int(input(f'ENTER THE MARK OF {t} : '))
   ma.append(m)
o=0
for i in ma:
    print(f'THE MARK OF {f[o]} is',i)
    o+=1
print(f'THE TOTAL MARK IS = {sum(ma)}')