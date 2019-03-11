class Employee:

    def __init__(self,name,empCode,pay):
        self.name=name
        self.empCode=empCode
        self.pay=pay

e1=Employee("Vineel",99,100000.00)
e2=Employee("Kumar",100,100000.00)

print("Name:",e1.name,"Code:",e1.empCode,"Pay:",e1.pay)
print("Name:",e2.name,"Code:",e2.empCode,"Pay:",e2.pay)

