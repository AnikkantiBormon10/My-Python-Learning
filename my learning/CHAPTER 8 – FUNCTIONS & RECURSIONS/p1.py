def greatest(a,b,c):
    if(b<a and c<a):
        return a
    if(b>a and c<b):
        return b
    else:
        return c
    
x = int(input("Enter number 1 : "))
y = int(input("Enter number 2 : "))
z = int(input("Enter number 3 : "))
gn=greatest(x,y,z)
print(f"greatest  numbers is : {gn}") 