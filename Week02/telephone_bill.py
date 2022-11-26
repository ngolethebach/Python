# Telephone Bill


while True:
    user_value = int(input("Enter number of minutes: "))
    if user_value <0:
        print("Error")
    else:
        print("Number of minutes used: ", user_value)
        basic_call_charge = 0.15 * user_value
        print("Basic call charge: £", basic_call_charge)
        vat_charge = (basic_call_charge/100)*20
        print("Vat due: £", vat_charge)
        total_charge = basic_call_charge + vat_charge
        print("Total bill: £", total_charge)
        break

