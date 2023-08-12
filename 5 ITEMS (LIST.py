prize  = []
item = ['item1','item2','item3','item4','item5']
for i in item:
   prize.append(int(input(f"ENTER THE PRIZE OF {i} : ")))
p=1
for i in prize:
   p=p*i
y=0
for i in item:
    print(f'THE PRIZE OF {i} IS RS.{prize[y]}')
    y+=1
print('THE SUM OF ALL ITEMS IS RS.',sum(prize),'\n','THE PROD OF ALL ITEMS IS RS.',p,'\n','THE AVERAGE OF ALL ITEMS IS RS.',sum(prize)/5)