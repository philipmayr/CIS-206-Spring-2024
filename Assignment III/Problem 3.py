# ASSIGNMENT III - CIS 206 - phil may'r

# Problem 3

def find_area_charge(ZIP_code):
    if ZIP_code == 60171:
        area_charge = 2.0
    elif ZIP_code == 60172:
        area_charge == 2.5
    elif ZIP_code == 60635:
        area_charge == 3.0
    else:
        area_charge == 5.0
    return area_charge
        
def find_weight_charge(package_weight):
    if package_weight > 50:
        weight_charge_factor = 0.03
        if package_weight > 100:
            weight_charge_factor = 0.02
    else:
        weight_charge_factor = 0.05
        
    weight_charge = weight_charge_factor * package_weight
    
    return weight_charge
            
def compute_postage(package_weight, ZIP_code, area_charge, weight_charge):
    postage = area_charge + weight_charge
    return postage
    
def display_postage_charges(area_charge, weight_charge, postage):
    print()
    print("Area Charge: " + "${:,.2f}".format(area_charge))
    print("Weight Charge: " + "${:,.2f}".format(weight_charge))
    print("Postage: " + "${:,.2f}".format(postage))

package_weight = int(input("Enter package weight in ounces: "))
ZIP_code = int(input("Enter area ZIP Code: "))
area_charge = find_area_charge(ZIP_code)
weight_charge = find_weight_charge(package_weight)
postage = compute_postage(package_weight, ZIP_code, area_charge, weight_charge)
display_postage_charges(area_charge, weight_charge, postage)
