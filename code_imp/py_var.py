## Var
print("--- Var ---")
def fun(a):
    print("func_in",id(a))   # func_in 41322472
    a = 2
    print(a)
    print("re-point",id(a), id(2))   # re-point 41322448 41322448

a = 1
print(a)  # 1
print("func_out",id(a), id(1))  # func_out 41322472 41322472

fun(a)

print(a)  # 1
print("func_out",id(a), id(1))  # func_out 41322472 41322472

# List
print("--- List ---")
def fun(a):
    print("func_in",id(a))  # func_in 53629256
    a.append(1)

a = []
print(a)
print("func_out",id(a))     # func_out 53629256

fun(a)

print(a) # [1]
print("func_out",id(a))