
#__init__ ... Konstruktor
# wird aufgerufen, wenn eine Instanz der Klasse erstellt wird

# self ist eine Referenz auf die Instanz selbst

#__str__ Repräsentation des Objekts

class Person:

    def __init__(self, firstname, lastname, age, isMale):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.isMale = isMale

    def __str__(self):
        return f"Firstname: {self.firstname}, Lastname: {self.lastname}, Age: {self.age}, isMale: {self.isMale}"


class Employee(Person):

    def __init__(self, firstname, lastname, age, isMale, salary):
        super().__init__(firstname, lastname, age, isMale)
        self.salary = salary

    def __str__(self):
        return super().__str__() + f"Gehalt: {self.salary}"


class DepartmentHead(Employee):

    def __init__(self, firstname, lastname, age, isMale, salary):
        super().__init__(firstname, lastname, age, isMale, salary)
        self.salary *= 4

    def __str__(self):
        return super().__str__()


class Department:

    def __init__(self, departmentName):
        self.departmentName = departmentName
        self.employees = []

    def __str__(self):
        return self.departmentName





































    

    class Department:

        def __init__(self, nameDepartment):
            self.nameDepartment = nameDepartment
            self.employees = []

        def __str__(self):
            return self.nameDepartment

        def addEmployee(self, employee):
            if isinstance(employee, DepartmentHead):
                for staff in self.employees:
                    if isinstance(staff, DepartmentHead):
                        print("Im Department: " + self.nameDepartment + " ist schon ein Department Head vorhanden")
                        return
                self.employees.append(employee)
            else:
                self.employees.append(employee)

        def countEmployees(self):
            return len(self.employees)

        def countDepartmentHeads(self):
            countDepartmentHeads = 0
            for i in self.employees:
                if isinstance(i, DepartmentHead):
                    countDepartmentHeads += 1
            return countDepartmentHeads

    class Company():

        def __init__(self, nameCompany):
            self.nameCompany = nameCompany
            self.departments = []

        def __str__(self):
            return self.nameCompany

        def addDepartment(self, department):
            self.departments.append(department)

        def countDepartments(self):
            return len(self.departments)

        def countEmployee(self):
            numberEmployees = 0
            for department in self.departments:
                numberEmployees += department.countEmployees()
            return numberEmployees

        def getBiggestDepartment(self):
            depSize = 0
            for i in self.departments:
                if i.countEmployees() > depSize:
                    depSize = i.countEmployees()
                    biggestDepartment = i
                else:
                    continue
            return biggestDepartment.nameDepartment

        def getMaleFemaleRatio(self):
            counterMale = 0
            for department in self.departments:
                for employee in department.employees:
                    if employee.isFemale == False:
                        counterMale += 1
                    else:
                        continue
            maleRatio = round((counterMale / self.countEmployee() * 100), 2)
            femaleRatio = round(100 - maleRatio, 2)
            return "in " + self.nameCompany + ": " + str(maleRatio) + "% of the employees are male and " + str(
                femaleRatio) + "% of the employees are female"

    def main():
        company = Company("DiyLed")
        dep1 = Department("Production")
        dep2 = Department("Marketing")
        dep3 = Department("Sales")
        emp1 = Employee("Jonas", "Kirchmair", "06.05.2005", False)
        emp2 = Employee("Julia", "Biechl", "01.09.2005", True)
        emp3 = Employee("Patrick", "Klaric", "29.11.2004", False)
        emp4 = Employee("Felix", "Haider", "29.11.2004", False)
        emp5 = Employee("Ian", "Hirschhuber", "29.11.2004", False)
        emp6 = Employee("Daniel", "Kopp", "29.11.2004", False)
        dph = DepartmentHead("Oliver", "Brandstetter", "25.06.2005", False)
        dph2 = DepartmentHead("Eva", "Bobchev", "25.06.2005", False)

        company.addDepartment(dep1)
        company.addDepartment(dep2)
        company.addDepartment(dep3)

        dep1.addEmployee(emp1)
        dep1.addEmployee(dph)
        dep1.addEmployee(dph2)
        dep1.addEmployee(emp2)
        dep2.addEmployee(emp3)
        dep2.addEmployee(emp4)
        dep3.addEmployee(emp5)
        dep3.addEmployee(emp6)

        print("Number of employees in department " + dep1.__str__() + " is: " + str(dep1.countEmployees()))
        print("Number of employees in department " + dep2.__str__() + " is: " + str(dep2.countEmployees()))
        print("Number of employees in department " + dep3.__str__() + " is: " + str(dep3.countEmployees()))
        print("Number of Department heads in department " + dep1.__str__() + " is: " + str(dep1.countDepartmentHeads()))
        print("Number of Department heads in department " + dep2.__str__() + " is: " + str(dep2.countDepartmentHeads()))
        print("Number of Department heads in department " + dep3.__str__() + " is: " + str(dep3.countDepartmentHeads()))
        print("Number of the employees in company " + company.__str__() + " is: " + str(company.countEmployee()))
        print("Department with the highest Number of employees is: " + company.getBiggestDepartment())
        print(company.getMaleFemaleRatio())

    if __name__ == "__main__":
        main()