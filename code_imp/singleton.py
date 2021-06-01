'''
单例是一种设计模式，应用该模式的类只会生成一个实例。

单例模式保证了在程序的不同位置都可以且仅可以取到同一个对象实例：如果实例不存在，会创建一个实例；如果已存在就会返回这个实例。因为单例是一个类，所以你也可以为其提供相应的操作方法，以便于对这个实例进行管理。

举个例子来说，比如你开发一款游戏软件，游戏中需要有“场景管理器”这样一种东西，用来管理游戏场景的切换、资源载入、网络连接等等任务。这个管理器需要有多种方法和属性，在代码中很多地方会被调用，且被调用的必须是同一个管理器，否则既容易产生冲突，也会浪费资源。这种情况下，单例模式就是一个很好的实现方法。
'''
## M1
import threading

class Singleton(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance


def test():
    single = Singleton()
    print(single)


for i in range(5):
    t = threading.Thread(target=test)
    t.start()


## M2
import threading


def singleton(cls):
    instances = {}

    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return _singleton


@singleton
def test(a, b):
    return None


def test1():
    print(test)


for i in range(5):
    t = threading.Thread(target=test1)
    t.start()


## M3
def singleton(cls):
    _instance = {}

    def inner():
        if cls not in _instance:
            _instance[cls] = cls()
        return _instance[cls]
    return inner
    
@singleton
class Cls(object):
    def __init__(self):
        pass

cls1 = Cls()
cls2 = Cls()
print(id(cls1) == id(cls2))


## M4
class Singleton(object):
    def __init__(self, cls):
        self._cls = cls
        self._instance = {}
    def __call__(self):
        if self._cls not in self._instance:
            self._instance[self._cls] = self._cls()
        return self._instance[self._cls]

@Singleton
class Cls2(object):
    def __init__(self):
        pass

cls1 = Cls2()
cls2 = Cls2()
print(id(cls1) == id(cls2))

class Cls3():
    pass

Cls3 = Singleton(Cls3)
cls3 = Cls3()
cls4 = Cls3()
print(id(cls3) == id(cls4))
