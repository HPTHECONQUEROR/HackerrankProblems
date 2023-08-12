class p:
    def __init__(self,x,y):
         self.x=x
         self.y=y
    def move(self):
       print("move")
    def draw(self):
        print("draw")


n=p(10,20)
print(n.y)