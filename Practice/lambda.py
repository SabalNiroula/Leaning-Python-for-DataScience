lst = [1, 34, 45, 44, 67, 76, 23]

lst1 = list((filter(lambda x: x>4 and x%2==0, lst)))
print(lst1)