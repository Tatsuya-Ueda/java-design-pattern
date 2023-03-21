class C():

    @property
    def x(self):
        pass
    
    def f(self):
        return self.x

class D():
    
    def x(self):
        return self

    def str(self):
        return "a"
    
    def __add__(self, s):
        return s + "d"
    def __radd__(self, s):
        return s + "d"

d = D()

print("".__add__(""))
print(d.__add__("a"))
print(d + "a")
print("a" + d)