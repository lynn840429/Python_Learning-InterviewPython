class Test(object):  
    num_of_instance = 0  

    def __init__(self, name, num):
        self.name = name
        self.num = num
        num += 1
        Test.num_of_instance += 1
  
if __name__ == '__main__':  
    print(Test.num_of_instance)   # 0
    t1 = Test('jack', 0)

    print(Test.num_of_instance)   # 1
    t2 = Test('lucy', 1)

    print(t1.name , t1.num, t1.num_of_instance)  # jack 2
    print(t2.name , t2.num, t2.num_of_instance)  # lucy 2
