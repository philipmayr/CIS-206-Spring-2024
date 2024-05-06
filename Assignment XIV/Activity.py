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
            
        short_term_bonus = self.compute_short_term_bonus()
        long_term_bonus = self.compute_long_term_bonus
            
    
    def set_job_level(self, job_level):
        self.job_level = job_level
        
        
    def get_job_level(self):
        return self.job_level
        
    
    def set_annual_salary(self, annual_salary):
        self.annual_salary = annual_salary
        
    
    def get_annual_salary(self):
        return self.annual_salary

    
    def compute_short_term_bonus(self):
        if self.job_level is not None and self.annual_salary is not None:
            if self.job_level == 'I':
                self.short_term_bonus = self.annual_salary * 0.25
            elif self.job_level == 'II':
                self.short_term_bonus = self.annual_salary * 0.20
            elif self.job_level == 'III':
                self.short_term_bonus = self.annual_salary * 0.10
            else:
                return None
        return self.short_term_bonus
        
        
    def compute_long_term_bonus(self):
        if self.annual_salary is not None:
            self.long_term_bonus = self.annual_salary * 0.10
        else:
            return None
        return self.long_term_bonus
        
            
    def print_attributes(self):
        if self.first_name is not None:
            print("First Name: " + str(self.first_name))
        if self.last_name is not None:
            print("Last Name: " + str(self.last_name))
        if self.job_level is not None:
            print("Job Level: " + str(self.job_level))
        if self.annual_salary is not None:
            print("Annual Salary: " + "{:,.2f}".format(self.annual_salary))
        if self.short_term_bonus is not None:
            print("Short Term Bonus: " + "{:,.2f}".format(self.short_term_bonus))
        if self.long_term_bonus is not None:
            print("Long Term Bonus: " + "{:,.2f}".format(self.long_term_bonus))


class Manager(Employee):
    pass
    
        
new_employee = Employee("Sam", "Bowman", 'I', 75000)
new_employee.print_attributes()
