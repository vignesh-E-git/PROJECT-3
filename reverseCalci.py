# REVERSED CALCULATOR
# ADD -> SUBTRACT
# SUB -> ADD
# MULTIPLY -> DIVIDE
# DIV -> MULTIPLY



class ModifyArithmeticOperation:
    def __init__(self,value):
        self.value = value
    def __add__(self,other): # sub
        res = ModifyArithmeticOperation(self.value - other.value)
        return res.value
    def __sub__(self,other): # add
        return ModifyArithmeticOperation(self.value + other.value).value
    def __mul__(self,other): # div 
        return ModifyArithmeticOperation(self.value / other.value)
    def __truediv__(self,other): # mult
        return self.value * other.value
    def __str__(self): # for printing x and y
        return str(self.value)
            

x = ModifyArithmeticOperation(5)
y = ModifyArithmeticOperation(1)


print(f'x : {x}\ny : {y}')

print(f'x+y : {x+y}')
print(f'x-y : {x-y}')  
print(f'x*y : {(x*y).value}')
print(f"x/y : {x/y}")
