from functools import lru_cache


class MyClass:
    field1 = 12
    field2 = 'hello'

    def my_method(self, p1, p2):
        self.field1 = p1 + p2

    def __init__(self):
        self.field3 = True

    def _privte_method(self, f2): # знак _ значит, что лучше не вызывать 
        self.field2 = f2


class Anceptor (MyClass):

    field4 = [1, 2, 3]

anceptor = Anceptor()
anceptor.my_method(3, 5)
print(anceptor.field1)
print(anceptor.field4)


#my_func = print 
#my_func('Hello World')

def make_operation(num1, num2, operation):
    return operation(num1, num2)


def add(p1, p2):
    return p1 + p2


print(make_operation(3, 4, add))

# 0, 1, 1, 2, 3, 5, 8, 13, 21...



def enter_exit(func):
    def wrapper(*args, **kwargs):
        print('Enter in function')
        res = func(*args, **kwargs) #** - это с именем в словарь (именнованый словарь) * - список args [4, 2, 6, 9, ........]
        print('Exit form function')
        return res
    
    return wrapper

@enter_exit
@lru_cache
def fibonacci(n):
    if n < 1:
        return 0
    
    if n == 1:
        return 1
    
    return fibonacci(n-1) + fibonacci(n-2)


