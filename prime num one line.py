primes = lambda q: (i for i in range(1,q) if i not in [j*k for j in range(1,i) for k in range(1,i)])
for i in primes(30):
      print(i)
