math = int(input())
eng = int(input())
his = int(input())

total = (math+eng+his)/3
print(total,"%")

if(total>40 and math>33 and eng>33 and his>33):
    print("pass")
else:
    print("faile")

