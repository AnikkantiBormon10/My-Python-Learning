def f_to_c(f):
    c=5*(f-32)/9
    print(f"{round(c,2)}'C")

f = int(input("Enter the value of F : "))
f_to_c(f)