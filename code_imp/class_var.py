class Test(object):  
    num_of_instance = 0  
    def __init__(self, name):  
        self.name = name  
        Test.num_of_instance += 1  
  
if __name__ == '__main__':  
    print(Test.num_of_instance)   # 0

    t1 = Test('jack')  
    print(Test.num_of_instance)   # 1

    t2 = Test('lucy')  
    print(t1.name , t1.num_of_instance)  # jack 2
    print(t2.name , t2.num_of_instance)  # lucy 2

    t3 = Test('lynn')
    print(t1.name , t1.num_of_instance)  # jack 3
    print(t2.name , t2.num_of_instance)  # lucy 3
    print(t3.name , t3.num_of_instance)  # lynn 3