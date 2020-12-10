# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x, y):
    if type(x) == int and type(y) == int:
        if x >= 0  and x <= 100  and y >= 0 and y <= 100:
            return x+y
        else:
            return("Please provide value between 0 to 100  ")
    else:
       return("Please provide interger only")

print(compute(2,3))
