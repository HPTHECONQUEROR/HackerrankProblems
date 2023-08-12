i=input(">> ")
o=i.split(" ")
e={  "happy":":)",'sad':':(','wow':':o'}
p=""
for i in o:
    p+=e.get('happy','ty')+ ""
print(p)