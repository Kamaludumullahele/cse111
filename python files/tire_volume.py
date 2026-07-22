## tire volume calcultion by user inputs
# volume = π*(w**2)*a*((w*a)+2540*d)/10000000000
# example tire size: 205/60R15 (w=205| a=60| d=15)
import math
π = math.pi
w = float(input("Enter the width of the tire in mm (ex 205): "))
a = int(input("Enter the aspect ratio of the tire (ex 60): "))
D = float(input("Enter the diameter of the wheel in inches (ex 15): "))
tire_volume = π*w**2*a*((w*a)+2540*D)/10000000000
print(f"The approximate tire volume is: {tire_volume:.2f} liters")
# input wheather the customer wants to byu the tire

        

# getting the date from the operating system
from datetime import datetime
current_datetime = datetime.now()
date_string = current_datetime.strftime("%Y-%m-%d")

# getting user input for tire purchase
while True:
    user_input = str(input("Do you want to buy this tire size? y/n: " )).lower()
    if user_input in ['yes','y']:
        name = str(input("please enter your name: "))
        phone_number = str(input("Enter your phone number? "))
        break
    elif user_input in ['no','n']:
        break

# opening a file for reading in text mode
#file = open("volumes.text")
with open ("volumes.txt", "at") as tire_file:
    print(f"{current_datetime}, {w}, {a}, {D}", file=tire_file)
    print(f"{name},{phone_number}",file=tire_file)

# tire prices for different sizes

if w==205 and a==60 and D==16:
    print(f"price for each tire size selected:$ 230")
elif w==225 and a==50 and D==18:
    print(f"price for each tire size selected:$ 300")
elif w==235 and a==40 and D==19:
    print(f"price for each tire size selected:$ 350")
elif w==255 and a==45 and D==20:
    print(f"price for each tire size selected:$ 450")
else: 
    print("Selected tire size is not available at the moment!")









    