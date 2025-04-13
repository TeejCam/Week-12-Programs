from Employee import Employee

emp1 = Employee("Susan Meyers", 47899, "Accounting", "Vice President")
emp2 = Employee("Mark Jones", 39119, "IT", "Programmer")
emp3 = Employee("Joy Rogers", 81774, "Manufacturing", "Engineer")

print(emp1.getName())
print(emp2.getId())
print(emp3.getPosition())

emp2.setName("Bob Dillan")
print(emp2.getName())
