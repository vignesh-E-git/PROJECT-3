class vector:
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        res_x = self.x + other.x
        res_y = self.y + other.y
        res_z = self.z + other.z
        return vector(res_x,res_y,res_z)
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y,self.z-other.z)
    def __mul__(self,other):
        return vector(self.x*other.x,self.y*other.y,self.z-other.z)
    def __truediv__(self,other):
        if other.x == 0 or other.y == 0 or other.z == 0:
            return 'ZERO DIVISION ERROR'
        return vector(self.x/other.x,self.y/other.y,self.z/other.z)
    def __str__(self):
        return str(f'({round(self.x,2)},{round(self.y,2)},{round(self.z,2)})')


v1 = vector(3,4,79)
v2 = vector(5,7,2)
v3 = vector(1,1)

print(f'vector addition : {v1+v3}')
print(f'vector subtraction : {v1-v2}')
print(f'vector multiplication : {v1*v2}')
print(f'vector division : {v1/v2}')


