def binary_search(list,item):
    low = 0
    high = len(list)-1
    while low<=high:
        mid = (low+high)//2
        print("low:%d, mid:%d, high:%d" %(low, mid, high))
        guess = list[mid]
        if guess>item:
            high = mid-1
        elif guess<item:
            low = mid+1
        else:
            return mid
    return None

mylist = [1,3,5,7,9]
print(binary_search(mylist,3))
print(binary_search(mylist,9))
print(binary_search(mylist,4))