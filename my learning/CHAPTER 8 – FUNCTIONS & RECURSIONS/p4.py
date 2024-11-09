def sum(n):
    if(n==1):
        return 1
    else:
        return n + sum(n-1)
x = int(input( "Enter a nu8mber : "))
print(sum(x))