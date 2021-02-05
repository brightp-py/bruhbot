x = 1

def foo():
    global x
    x += 1
    return x

print(foo())
print(x)