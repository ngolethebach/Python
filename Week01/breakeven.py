#breakeven


item_cost = float(input("Cost to produce each item: "))
sale_price = float(input("Sale price for each item: "))
fixed_cost = float(input("Fixed cost: "))
profit_per_item = sale_price - item_cost
print("Profit per item: ", profit_per_item)
break_even = fixed_cost/(sale_price - item_cost)
print("Breakeven: ", break_even, "items")
