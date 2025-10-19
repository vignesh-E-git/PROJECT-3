#x - real number
# y - complex number

class ComlexCalci:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self,other):
        re = self.x + other.x
        im = self.y + other.y
        return f'addition : {re}+{im}i'
    def __sub__(self,other):
        re = self.x - other.x
        im = self.y - other.y
        return f'subtraction : {re}+{im}i'
    def __mul__(self,other):
        re = self.x*other.x - self.y*other.y
        im = self.x*other.y + self.y*other.x
        return f'multiplication : {re}+{im}i'
    def __truediv__(self,other):
        cons = other.x**2 + other.y**2
        re = self.x*other.x + self.y*other.y
        im = self.x*other.y - self.y*other.x
        return f'division : 1/{cons}({re}+{im}i)'
    
c1 = ComlexCalci(2,4)
c2 = ComlexCalci(5,9)
print(c1+c2)
print(c1-c2)
print(c1*c2)
print(c1/c2)