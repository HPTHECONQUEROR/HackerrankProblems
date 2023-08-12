#STRINGS
c="HARI'S FAV GAME IS GTA 5"
v='MY FAV  GAME IS "GTA 5"'
m='''HELLO HARI.
I AM HARI.
HOW ARE YOU .
I AM FINE'''
q='HELLO HARI. \nI AM HARI.\nHOW ARE YOU .\nI AM FINE'
s='I LOVE MY MOM'
print(s[0:5])
print(s[-2])


#EX FOR MATTED STRINGS
q='hari'.upper()
p='prasath'.upper()
print(f'HI MY NAME IS {q} {p}')

#STRINGS METHODS
q='I LOVE  MY MOM\n'
print(len(q))
print(q.upper())
print(q.lower())
print(q.find("M"))
print(q.title())
print(q.replace('MOM','DAD'))
print('python' in q,"MOM"in q)