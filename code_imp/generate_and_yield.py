mylist = [x*x for x in range(3)]

for i in mylist:
    print("mylist=", i)

for i in mylist:
    print("mylist=", i)

for i in mylist:
    print("mylist=", i)

#-----------------------------------------
mygenerator = (x*x for x in range(3))

for i in mygenerator:
    print("mygenerator=", i)

for i in mygenerator:
    print("mygenerator=", i)

for i in mygenerator:
    print("mygenerator=", i)


def create_generator():
    mylist = range(3)
    for i in mylist:
        yield i*i

#-----------------------------------------
mygenerator_y = create_generator() # create a generator
print(mygenerator_y) # mygenerator is an object!

for i in mygenerator_y:
    print("mygenerator_y=", i)

for i in mygenerator_y:
    print("mygenerator_y=", i)

for i in mygenerator_y:
    print("mygenerator_y=", i)
