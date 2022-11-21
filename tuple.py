x = (10, 20, 30, 40, 50)
new = (90,)
pos = 4

y = x[:pos-1]
y = y+new
x = y+x[pos-1:]
print(x)