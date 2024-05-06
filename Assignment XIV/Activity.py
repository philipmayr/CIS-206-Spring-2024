# ASSIGNMENT XIV - CIS 206 - phil may'r

class Employee:
    
    def __init__(self, first_name=None, last_name=None, job_level=None, annual_salary=None):
        self.short_term_bonus = None
        self.long_term_bonus = None
        
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if job_level is not None:
            self.job_level = job_level
        if annual_salary is not None:
            self.annual_salary = annual_salary
            
            
    def compute_short_term_bonus(self, job_level, annual_salary):
        if job_level is not None and annual_salary is not None:
            if job_level == 'I':
                self.short_term_bonus = annual_salary * 0.25
            elif job_level == 'II':
                self.short_term_bonus = annual_salary * 0.20
            elif job_level == 'III':
                self.short_term_bonus = annual_salary * 0.10
            else:
                return None
        return self.short_term_bonus
        
        
    def compute_long_term_bonus(self, job_level, annual_salary):
        if annual_salary is not None:
            self.long_term_bonus = annual_salary * 0.10
        else:
            return None
        return self.long_term_bonus
        
            
    def print_attributes(self):
        print("First Name: " + str(self.first_name))
        print("Last Name: " + str(self.last_name))
        print("Job Level: " + str(self.job_level))
        print("Annual Salary: " + "{:,.2f}".format(self.annual_salary))
        print("Short Term Bonus: " + "{:,.2f}".format(self.short_term_bonus))
        print("Long Term Bonus: " + "{:,.2f}".format(self.long_term_bonus))


class Manager(Employee):
    pass
    
        
new_employee = Employee("Sam", "Bowman", 'I', 75000)
new_employee.compute_short_term_bonus(new_employee.job_level, new_employee.annual_salary)
new_employee.compute_long_term_bonus(new_employee.job_level, new_employee.annual_salary)
new_employee.print_attributes()
