import re

class Employee:

    def __init__(self, name):
        self.name = name

    
    def name_validation(self):
        regex = r"[^a-zA-Z0-9]"
        match = re.search(regex, self.name)

        if match != None:
            print("Name is macthing with the pattern")
            match = re.split(regex, self.name) 
            
            self.firstname = match[0]
            self.lastname = match[1]

            print("First Name: ",self.firstname)
            print("Last Name: ", self.lastname)

        else:
            print("Name is does not macthing with the pattern")



employee = Employee("John#Denkmark")
employee.name_validation()
    