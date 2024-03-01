# ASSIGNMENT VII - CIS 206 - phil may'r

import csv

def compute_gross_pay(hours, rate):
    overtime_rate = rate * 1.5
    regular_hours = hours - (hours % 40)
    overtime_hours = hours % 40
    gross_pay = (regular_hours * rate) + (overtime_hours * overtime_rate) 

    return gross_pay

def format_email_address(last_name, first_name):
    address = first_name[0].lower() + last_name.lower() + '@' + "gm.com"
    
    return address

try:
    with open('EmpData.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        with open('NewEmpData.csv', 'w', newline='') as new_csv_file:
            fieldnames = ["Last_Name", "First_Name", "Gross_Pay", "EMail"]

            writer = csv.DictWriter(new_csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for line in reader:
                last_name = line['Last_Name']
                first_name = line['First_Name']
                hours = float(line['Hours'])
                rate = float(line['Rate'])

                gross_pay = compute_gross_pay(hours, rate)
                email_address = format_email_address(last_name, first_name)

                name = {"Last_Name": last_name, 
                        "First_Name": first_name, 
                        "Gross_Pay": gross_pay, 
                        "EMail": email_address}

                writer.writerow(name)
except IOError:
    print("Read/Write Error")
except:
    print("Unknown Error")
