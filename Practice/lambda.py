#before lambda we do like this
def square(a, b):
    return a+b;


sq = lambda x: "Even" if x % 2 == 0 else "Odd"

print(sq(10))
print(sq(20))