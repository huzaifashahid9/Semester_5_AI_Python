def compute_units_cost(units):

    if units <= 100:
        return units * 12

    elif units <= 300:
        first_slab = 100 * 12
        remaining_units = units - 100
        second_slab = remaining_units * 18
        return first_slab + second_slab

    else:
        first_slab = 100 * 12
        second_slab = 200 * 18
        remaining_units = units - 300
        third_slab = remaining_units * 25
        return first_slab + second_slab + third_slab

def compute_bill(units, tax_rate=0.17, fixed_charge=150):

    slab_cost = compute_units_cost(units)
    tax = slab_cost * tax_rate
    total = slab_cost + tax + fixed_charge
    return slab_cost, tax, fixed_charge, total

def print_bill(units, tax_rate=0.17, fixed_charge=150):

    slab_cost, tax, fixed_charge, total = compute_bill(
        units, tax_rate, fixed_charge
    )

    print("\n------ ELECTRICITY BILL ------")
    print("Units:", units)
    print("Slab Cost:", slab_cost)
    print("Tax:", tax)
    print("Fixed Charge:", fixed_charge)
    print("Total:", total)

units_entered = input("Enter electricity units: ")

if not units_entered.isdigit():
    print("Invalid input! Please enter a numeric value.")

else:
    units = int(units_entered)

    if units < 0:
        print("Units cannot be negative.")
        
    else:
        print_bill(units)
        print_bill(units, tax_rate=0.10)
        print_bill(units, tax_rate=0.05, fixed_charge=200)