import csv
from datetime import datetime, timedelta, date
import datetime as dt



QUANTITY_INDEX = 1
def main ():
    PRODUCT_INDEX = 0
    NAME_INDEX = 1
    PRICE_INDEX = 2
    try:
        products_dict = read_dictionary("products.csv", PRODUCT_INDEX)

        with open ("request.csv", "rt") as request_file:
            reader = csv.reader(request_file)
            next(reader)
            print("Cornerave Grocery Store")
            num_items = 0
            sub_total = 0
            sales_tax = 0
            total = 0

            for row in reader:
                if not row:
                    continue
                try:
                    product_number = row[PRODUCT_INDEX]
                    quantity = int(row[QUANTITY_INDEX])
                    if product_number in products_dict:
                        num_items += quantity
                    #else: 
                        #print("items is not added to quantity")
                    

                    # using the product_num to find the item
                    # from the products_dict
                    product_info = products_dict[product_number]
                    product_name = product_info[NAME_INDEX]

                    product_price = float(product_info[PRICE_INDEX])
                    cost_for_each_item = product_price * quantity
                    sub_total += cost_for_each_item
                    sales_tax = sub_total * 6 / 100
                    total = sub_total + sales_tax

                    print(f"{product_name}: {quantity} @ {product_price}")
                except KeyError:
                    print(f"unknown product ID({product_number}) in the request.csv file")
                except ValueError:
                    print(f"Invalid quantity in request.csv for product {product_number}")

    except FileNotFoundError as not_found_err:
        print(f"Error: missing file - {not_found_err.filename}")
        return
    except PermissionError as not_permitted_err:
        print(f"Error: {not_permitted_err}")
        return

    print(f"Number of items:",num_items)
    print(f"Subtotal: {sub_total:.2f}")
    print(f"Sales tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    print("Thank you for shopping at Cornerave Grocery Store")
    now = datetime.now()
    # Exceeded requirment
    today = datetime.now()
    future_day = today + timedelta(days=30)
    today = date.today()
    target_date = date(2027, 1, 1)
    difference = (target_date - today).days
    print(now.strftime("%a %b %e %H:%M:%S %Y"))
    # exceeded requirement
    print(f"Ruturn by: at 9.00 pm", future_day.strftime("%Y-%m-%d"))
    print(f"Days to New Year Sales Begins: {difference} days")


def read_dictionary(filename, key_column_index):
    # create an empty dictionary that stores data
    # from csv file
    dictionary = {}
    #Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open (filename, "rt") as csv_file:
    # creating a reader object fromm the csv module to 
    # read the opened csv file
        reader = csv.reader(csv_file)
        next(reader)
        for product_list in reader:
            if len(product_list) != 0:
                key = product_list[key_column_index]
                dictionary[key] = product_list
    return dictionary




if __name__ == "__main__":
    main()