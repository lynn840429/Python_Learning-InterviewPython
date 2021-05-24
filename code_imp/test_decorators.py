# def printHello(func):
#     def wrapper(*args, **kwargs):
#         print('Hello')
#         return func(*args, **kwargs)
#     return wrapper

# @printHello
# def printSingle(arg):
#     print(arg)

# @printHello
# def printDouble(arg1, arg2):
#     print(arg1)
#     print(arg2)

# printSingle('World')
# printDouble('Kitty', 'Danny')


def before(func):
    #  只能通过参数声明的方式获取参数
    def check(a, *args):
        # 如果小于0，抛出异常
        if(a < 0):
            raise Exception('a is less than zero!')
        else:
            return func(a, *args)
    # 记住，返回的一定是函数            
    return check

@before
def add (a, b):
    return a + b

# 自动会抛出错误
print(add(31, 2))