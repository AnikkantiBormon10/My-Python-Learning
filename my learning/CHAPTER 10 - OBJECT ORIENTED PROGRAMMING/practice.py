#A class is a blueprint for creating object
# class Student :
#     uni = "MU"
#     batch = 55
#     department = "CSE"

    

# anik = Student()
# anik.name="Anik"
# print(anik.name, anik.uni, anik.batch)
# himel = Student()
# himel.name="Himel"
# print(himel.name, himel.department, himel.batch)

# METHOD

class Student :
    uni = "MU"
    batch = 55
    department = "CSE"
    def getinfo(salf):
        print(f"the Univarsity is {salf.uni} and the batch is {salf.batch} and The department is {salf.department}  ")


anik = Student()
anik.name="Anik"
print(anik.name, anik.uni, anik.batch)
himel = Student()
himel.name="Himel"
print(himel.name, himel.department, himel.batch)

anik.getinfo()