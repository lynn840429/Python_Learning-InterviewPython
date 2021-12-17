class D(object):
    def __init__(self):
        self.a = 1
    def foo1(self):
        print("D")

class B(D):
    pass

class C(D):
    def __init__(self):
        self.a = 2
    def foo1(self):
        print("C")

class A(B, C):
    pass

a = A()
print(a.a)

# d = D()
# d.foo1()