# Normal class "Person"
class Person():
    def __init__(self, name):
        self.name = name
    
    def say_name(self):
        print(f"My name is {self.name}.")

# Class Employee inherits from Person 
class Employee(Person):
    def __init__(self, name, salary):  
        super(Employee, self).__init__(name)   # Constructor of Employee does super.__init__ to use the constructor of Person and then does the extra instructions personalized for Employee.
        self.salary = salary

    def say_salary(self):
        print(f"My salary is {self.salary}.")


frank = Employee("Frank", 1500) # Creating a new employee
frank.say_name() # Employee can use methods of the parent class, in this case "Person"
frank.say_salary()