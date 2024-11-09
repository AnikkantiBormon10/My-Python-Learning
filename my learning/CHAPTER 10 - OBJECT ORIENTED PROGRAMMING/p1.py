#1. Create a class “Programmer” for storing information of few programmers working at Microsoft.
import random
class Programmer:
    company = random.choice(["microsoft","facebook","google","TATA"])
    def __init__(self, name , lang, salary):
        self.name=name
        self.lang=lang
        self.salary=salary
        print(f"Employee name is {self.name} langluage is {self.lang} salary is {self.salary} and company is {self.company}")   
x=random.choice(["babaji ka tulu",50000 , 100000,200000,500000000,"Zero"])
a=Programmer("Anik","py",x)
print(a)