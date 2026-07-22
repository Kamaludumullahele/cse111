import datetime
today=datetime.date.today()
dow= today.weekday()

subtotal=0
quantity=1

while quantity !=0: 
    quantity = int(input("what is the quantity? "))
    if quantity !=0:
        price = float(input("Price of the item? "))
        subtotal += float(quantity * price)
print(f"Total order: $ {subtotal}")
DISCOUNT_RATE=.1
TAX_RATE=.06
discount=0
if dow == 2 or dow == 3 or dow == 0:
    if subtotal >= 50:
        discount = round(subtotal * DISCOUNT_RATE,2)
        print(f"Discount amount:$ {discount}")
    else:
        short = 50 - subtotal
        print(f"You are $ {short:.2f} from your discount")
subtotal -= discount
tax = round(subtotal * TAX_RATE,2)
total = round(subtotal + tax,2)
print(f"Subtotal:$ {subtotal:.2f}")
print(f"Tax:$ {tax:.2f}")
print(f"Total Due:$ {total:.2f}")
