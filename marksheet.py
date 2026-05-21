sub1 = int(input("Subject 1 marks: "))
sub2 = int(input("Subject 2 marks: "))
sub3 = int(input("Subject 3 marks: "))

total = sub1 + sub2 + sub3
percentage = (total / 300) * 100

print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
