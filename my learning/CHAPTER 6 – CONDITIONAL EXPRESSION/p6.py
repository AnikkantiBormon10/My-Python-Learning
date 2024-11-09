mark = int(input("Enter the mark : "))

if(mark<101 and mark>89):
    print("EX")
elif(mark<90 and mark>79):
    print("A")
elif(mark<80 and mark>69):
    print("b")
elif(mark<70 and mark>59):
    print("C")
elif(mark<60 and mark>49):
    print("D")
elif(mark<50):
    print("F")
else:
    print("You enter invalid mark")