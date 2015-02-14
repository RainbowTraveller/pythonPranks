from Employee import Empl
from ITEmployee import ITEmpl

e = Empl("Milind", 30)
print e.getAge()
print e.getName()
ie = ITEmpl("Milind", 30, "worker", 50, "No.2")
print ie.getAge()
print ie.getName()
print ie.getSalary()
print ie.getPlatform()
print ie.getPost()



