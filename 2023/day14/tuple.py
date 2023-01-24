list1= ['History','Geography','Maths','Science']
list2= list1
#list are mutable tuples are immutable
list1[0]='Computer'
print(list1)
print(list2)
# by changing list 1 the list 2 value also changed so we can use tuple instead of list
#let's convert list to tuple
tup1=tuple(list1)
tup2=tup1
tup1[0]='History' #type error
print(tup1)
print(tup2)