list2 = [1, 34, 45, 44, 67, 76, 23]

lst = list(map(lambda x: x*2 if (x%2==0) else x*3, list2))
print(lst)