class human:
    def __init__(self,name,salary,age):
        self.__salary = 0.0
        self.__name = ""
        self.__age = 0
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def getSalary(self):
        return self.__salary
    def setName(self,name):
        self.__name = name
    def setAge(self,age):
        self.__age = age
    def setSalary(self,salary):
        self.__salary = salary
    def show(self):
        print(f"Имя:{self.__name}\n зарплата: {self.__salary}\n  возраст:{self.__age}")
class employee(human):
    def __init__(self,company):
        self.__company = ""
    def getCompany(self):
        return self.__company
    def setCompany(self,company):
        self.__company = company


Bob = human("Oleg",12.3,22)
Bob.show()
Bob.setName("Bob")
Bob.setAge(22)
Bob.setSalary(122.25)
Bob.show()
Tom = employee("Google")
Tom.setName("Tom")
Tom.setAge(19)
Tom.setSalary(2112.12)
Tom.setCompany("Google")
Tom.show()
print(f"Название компании: {Tom.getCompany()}")