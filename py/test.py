class Vector:

    def __init__(self, a, b, z):
       self.a = a
       self.b = b
       self.z = z

    def add(p1, p2):
        return (p1.a + p2.a, p1.b + p2.b)
    def sub(p1,p2):
        return (p1.a - p2.a, p1.b - p2.b)
    def mul(p1,p2):
        return (p1.a * p1.a + p2.b * p2.b)

    
v1 = Vector(1,2)
v2 = Vector(4,5)
print(v1.add(v2))
print(v1.sub(v2))
print(v1.mul(v2))