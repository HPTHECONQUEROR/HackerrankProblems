import  random


class dice:


    def roll(self):


        r=random.randint(1,6)
        r2=random.randint(1, 6)
        return r,r2


e=dice()


print(e.roll())