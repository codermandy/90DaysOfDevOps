s={2,4,3,6,2,6,}
print(s)
#sets take value only once, do not contain duplicates
#can hold multiple values of different types
#order is not important
info={"carla",19,False,4.8,10}
print(info)

harry=set()
print(type(harry))

for value in info:
    print(value)

    #set methods
s={1,2,6,4,7}
s2={3,5,9,0}
print(s.update(s2))
print(s)
s.add(32)
s.remove(2)
del(s2)