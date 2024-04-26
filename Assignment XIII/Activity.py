class Employee:
    
    def __init__(self, first_name, last_name, job_level, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.job_level = job_level
        self.annual_salary = annual_salary
        if job_level == 1:
            self.short_term_bonus = annual_salary * 0.25
        elif job_level == 2:
            self.short_term_bonus = annual_salary * 0.20
        elif job_level == 3:
            self.short_term_bonus = annual_salary * 0.10
        self.long_term_bonus = annual_salary * 0.10
        
new_employee = Employee("Sam", "Bowman", 1, 70000)

print(new_employee.first_name)
print(new_employee.last_name)
print(new_employee.job_level)
print(new_employee.annual_salary)
print(new_employee.short_term_bonus)
print(new_employee.long_term_bonus)
