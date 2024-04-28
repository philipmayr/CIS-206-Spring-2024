class Employee:
    
    def __init__(self, first_name=None, last_name=None, job_level=None, annual_salary=None):
        self.first_name = None
        self.last_name = None
        self.job_level = None
        self.annual_salary = None
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
        if job_level is not None and annual_salary is not None:
            if job_level == 1:
                self.short_term_bonus = annual_salary * 0.25
            elif job_level == 2:
                self.short_term_bonus = annual_salary * 0.20
            elif job_level == 3:
                self.short_term_bonus = annual_salary * 0.10
        if annual_salary is not None:
            self.long_term_bonus = annual_salary * 0.10
        
new_employee = Employee("Sam", "Bowman", 1, 70000)

print(new_employee.first_name)
print(new_employee.last_name)
print(new_employee.job_level)
print(new_employee.annual_salary)
print(new_employee.short_term_bonus)
print(new_employee.long_term_bonus)
