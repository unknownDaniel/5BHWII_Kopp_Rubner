#- Bitte UML-Klassendiagramm zeichnen

#- eine Firma
#- Es gibt Personen, Mitarbeiter, Abteilungsleiter
#- Es gibt mehrere Abteilungen, jede(r) Mitarbeiter ist in einer Abteilung
#- Es gibt beide Geschlechter
#- es gibt nur einen Abteilungsleiter pro Abteilung
#- Mitarbeiter gehören immer zu einer Abteilung
#- ein Abteilungsleiter ist auch ein Mitarbeiter

#- modelliere die Objekte über Vererbung
#- erzeuge zum Schluss ein Firmenobjekt

# programmiere folgende Methoden:
 #- man muss alle Objekte instanzieren können
 #- wieviele Mitarbeiter, Abteilungsleiter gibts in der Firma
 #- wieviel Abteilungen gibt es
 #- welche Abteilung hat die größte Mitarbeiterstärke
 #- wie ist der Prozentanteil Frauen Männer

#Maximiere die Logik-Kapselung...Methoden und Datenstrukturen sollten in den passenden Klassen implementiert werden.



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

    def addEmployee(self, employee):
        if isinstance(employee, DepartmentHead):
            # Wenn der hinzuzufügende Mitarbeiter ein DepartmentHead ist
            for staff in self.employees:
                if isinstance(staff, DepartmentHead):
                    print(f"In der Abteilung: {self.departmentName} ist schon ein Abteilungsleiter vorhanden")
                    return
            self.employees.append(employee)
        else:
            self.employees.append(employee)


    def countEmployee(self):
        return len(self.employees)

    def countDepartmentHead(self):

        countDeparmentHead = 0
        for i in self.employees:
            if isinstance(i, DepartmentHead):
                countDeparmentHead += 1
        return countDeparmentHead


class Company:

    def __init__(self, companyName):
        self.companyName = companyName
        self.departments = []

    def __str__(self):
        return self.companyName

    def addDepartment(self, department):
        self.departments.append(department)

    def countDepartment(self):
        return len(self.departments)

    def countEmployees(self):
        numberEmployee = 0
        for department in self.departments:
            numberEmployee += department.countEmployee()
        return numberEmployee


    def getBiggestDepartment(self):
        departmentSize = 0
        biggestDepartment = None

        for i in self.departments:
            if i.countEmployee() > departmentSize:
                departmentSize = i.countEmployee()   # Aktualisiere die Größe der größten Abteilung
                biggestDepartment = i
        if biggestDepartment is not None:
            return biggestDepartment.departmentName
        else:
            return "Es gibt keine Abteilungen."


    def getMaleOrFemaleRatio(self):
        counterMale = 0
        for department in self.departments:
            for employee in department.employees:
                if employee.isMale:
                    counterMale += 1

        maleRatio = round((counterMale / self.countEmployees() * 100), 2)
        femaleRatio = round(100 - maleRatio, 2)
        return f"In {self.companyName}: {maleRatio}% der Angestellten sind männlich und {femaleRatio}% der Angestellten sind weiblich."

def main():
        company = Company("Yandex")

        dep1 = Department("GameDesing")
        dep2 = Department("Modellierung")
        dep3 = Department("SoundDesign")

        company.addDepartment(dep1)   #(dep1, dep2, dep3)
        company.addDepartment(dep2)
        company.addDepartment(dep3)

        emp1 = Employee("Johannes", "Adami", "19", True, 1500)
        emp2 = Employee("David", "Chech", "48", True, 5600)
        emp3 = Employee("Eva", "Bobochev", "18", False, 470)
        emp4 = Employee("Pasha", "Khakhlou", "19", True, 1850)
        emp5 = Employee("Daniel", "Kopp", "19", True, 2800)
        emp6 = Employee("Patrick", "Klaritsch", "19", True, 2980)

        dph1 = DepartmentHead("Julia", "Biechl", "18", False, 2500)
        dph2 = DepartmentHead("Ian", "Hirschuber", "19", True, 2500)


        dep1.addEmployee(emp1)
        dep1.addEmployee(emp2)

        dep2.addEmployee(dph1)
        dep2.addEmployee(dph2)
        dep2.addEmployee(emp3)

        dep3.addEmployee(emp4)
        dep3.addEmployee(emp5)
        dep3.addEmployee(emp6)


        print(f"In der Abteilung {dep1} sind {dep1.countEmployee()} Angestellte")
        print(f"In der Abteilung {dep2} sind {dep2.countEmployee()} Angestellte")
        print(f"In der Abteilung {dep3} sind {dep3.countEmployee()} Angestellte")

        print(f"In der Firma {company} sind {company.countEmployees()} Angestellte")
        print(f"Die größte Abteilung ist: {company.getBiggestDepartment()}")
        print(company.getMaleOrFemaleRatio())

if __name__ == "__main__":
    main()


