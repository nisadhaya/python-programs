num = int(input("Enter a number: "))
temp = num
sum_digits = 0
num_digits = len(str(num))

while temp > 0:
    digit = temp % 10
    sum_digits += digit ** num_digits
    temp //= 10

if num == sum_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
