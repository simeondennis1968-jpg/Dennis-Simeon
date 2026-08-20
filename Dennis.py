# ----- Customer Information ----
customer_name = input("Enter Customer Name: ")
contact_number = input("Enter Contact Number: ")
address = input("Enter Address: ")
print("\nProduct 1")
product1_name = input("Enter Product 1 Name: ")
product1_price = float(input("Enter Price: "))
product1_qty = int(input("Enter Quantity: "))
product1_amount = product1_price * product1_qty
print("\nProduct 2")
product2_name = input("Enter Product 2 Name: ")
product2_price = float(input("Enter Price: "))
product2_qty = int(input("Enter Quantity: "))
product2_amount = product2_price * product2_qty
print("\nProduct 3")
product3_name = input("Enter Product 3 Name: ")
product3_price = float(input("Enter Price: "))
product3_qty = int(input("Enter Quantity: "))
product3_amount = product3_price * product3_qty
discount = 10.0 
subtotal = product1_amount + product2_amount + product3_amount
discount_amount = subtotal * (discount / 100)
total_amount = subtotal - discount_amount

# -----  Receipt Output ------
print("\n=========================================")
print("               STORE RECEIPT")
print("=========================================")
print(f"Customer Name : {customer_name}")
print(f"Contact No.   : {contact_number}")
print(f"Address       : {address}")
print("\n-----------------------------------------")
print(f"{'Product':<15}{'Price':>8}{'Qty':>6}{'Amount':>10}")
print("-----------------------------------------")
print(f"{product1_name:<15}{product1_price:>8.2f}{product1_qty:>6}{product1_amount:>10.2f}")
print(f"{product2_name:<15}{product2_price:>8.2f}{product2_qty:>6}{product2_amount:>10.2f}")
print(f"{product3_name:<15}{product3_price:>8.2f}{product3_qty:>6}{product3_amount:>10.2f}")
print("-----------------------------------------")
print(f"{'Subtotal':<21}{subtotal:>18.2f}")
print(f"{'Discount (' + str(discount) + '%)':<21}{discount_amount:>18.2f}")
print("-----------------------------------------")
print(f"{'TOTAL':<21}{total_amount:>18.2f}")
print("=========================================")
print("\nThank you for your purchase!")
print("Please come again!")