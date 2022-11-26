# Cost of living 


rent_per_month = float(input("Rent per month: "))
gas_per_month = float(input("Gas payment per month: "))
electricity_per_month = float(input("Electricity payment per month: "))
water_per_month = float(input("Water payment per month: "))
council_tax_per_month = float(input("Council tax per month: "))
total = round(rent_per_month + gas_per_month + electricity_per_month + water_per_month + council_tax_per_month,2)


print("Your monthly expenses are: ")
print("Rent:                £ ", rent_per_month)
print("Gas:                 £ ", gas_per_month)
print("Electricity:         £ ", electricity_per_month)
print("Water:               £ ", water_per_month)
print("Council tax:         £ ", council_tax_per_month)
for i in range(2):
    print("=" * 30)
print("Total:               £ ", total)
print("=" * 30)
