#this is example of using varargs

def display(var, **kargs):
    print("formal argument:", var)

    for x,y in kargs.items():
        print("key = {}, value = {}".format(x, y))

display(10, name= "aroghya")