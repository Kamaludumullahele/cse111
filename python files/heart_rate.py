# optimal heart rate calculator

# max heart rate = 220 - age

age = int(input("Enter your age: "))
max_heart_rate = 220 - age

# print the maximum heart rate using an f-string

print(f"Your maximum heart rate is: {max_heart_rate} beats per min")
print()

# calculte the 65% and 85% of the maximum heart rate
lower = max_heart_rate * 65/100
upper = max_heart_rate * 85/100

# print the lower and upper limits using an f-string

print(f"""When you exercise to strengthen your heart, you should
keep your heart rate between {lower:.0f} and {upper:.0f} beats per minute""")
print()
