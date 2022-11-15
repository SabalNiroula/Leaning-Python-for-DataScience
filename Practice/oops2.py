class Sample:

   x = 10

   @classmethod
   def modify(change):
    change.x+=10

    def display():
        print("value of x", x)

s1 = Sample()
s2 = Sample()

print("value of x", s1.x)
print("value of x", s2.x)


s1.modify()
print("value of x", s1.x)
print("value of x", s2.x)

