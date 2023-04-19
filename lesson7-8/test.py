class Cl:
    def __init__(self,i,b):
        self.i = i
        self.b = b

    def dod(self):
        print(self.i + self.b)

cl = Cl(i = 5,b=5)
cl.dod()