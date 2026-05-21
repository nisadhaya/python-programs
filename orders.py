product = input("Enter product name: ")
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))

total_cost = price * quantity
print(f"\nOrder Summary:\nProduct: {product}\nTotal Cost: ${total_cost:.2f}")
