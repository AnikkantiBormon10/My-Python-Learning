s = {1, 5, 32, "Anik"}
se = {} #This Not Empty 'set' it's empty "dictionary"
e= set() #this is Empty set 
s1={1,5,8,6,6,4,7,5}
print(s,se,e)
print(s1)# set can't store dublicate value
s.add("pulok")
print(s)
print(s.union(s1))
print(s.intersection(s1))
print(s.issubset(s1))
print(s.issuperset(s1))
print(s.isdisjoint(s1))

