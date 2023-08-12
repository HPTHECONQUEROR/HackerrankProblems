o=15
for i in range(2,o):
    if o%i==0:
        print('not prime')
        break
    elif o%i !=0 :
        print("prime")
        break
    else:
        ('neither prime nor composite')
if o==1 or o==2:
    print("neither prime nor composite")
