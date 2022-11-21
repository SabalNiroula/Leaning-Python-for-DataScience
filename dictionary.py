x = {}

n = int(input("How many players ? "))

for i in range(n):
    name = input("Enter player name: ")
    run = int(input("Enter runs: "))
    x.update({name:run})

print("\nThe player in the team")
for k in x.keys():
    print(k)

name = input("Enter name to get runs: ")
run = x.get(name, -1)
if (run == -1):
    print ("you entered wrong name!")
else:
    print("{} made {} runs".format(name, run))