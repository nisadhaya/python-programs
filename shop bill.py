items_count = int(input("How many items did you buy? "))
total_bill = 0

for i in range(items_count):
    price = float(input(f"Enter price for item {i+1}: "))
    total_bill += price

print(f"\nTotal Bill Amount: ${total_bill:.2f}")
