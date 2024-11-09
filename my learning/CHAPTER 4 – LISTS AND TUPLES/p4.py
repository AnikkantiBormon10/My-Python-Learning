numbers=[]
for i in range(4):
    i = int(input("Enter Number : "))
    numbers.append(i)
    numbers.sort()

print(numbers)
print(sum(numbers))