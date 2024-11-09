num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))
num4 = int(input("Enter 4th number : "))

if(num2<num1 and num3<num1 and num4<num1):
    print("Gratest Number is : ", num1)
elif(num1<num2 and num3<num2 and num4<num2):
    print("Gratest Number is : ", num2)
elif(num2<num3 and num1<num3 and num4<num3):
    print("Gratest Number is : ", num3)
else:
    print("Gratest Number is : ", num4)


