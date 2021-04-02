print("====================computerbazar===================")
print("do you want to buy computer \n press y or Y if yes ")
choice = input("Enter your choice")
if choice == 'y' or choice == 'Y':
    computer = int(input("""\t\t\t\t\twhich computer do you want to buy press
       \t\t\t\t\t1. dell price(Rs.20000)
       \t\t\t\t\t2. mac price(Rs.50000)
       \t\t\t\t\t3. toshiba price (Rs.20000)
       """))
    if computer == 1:
        price = 20000
    elif computer == 2:
        price = 50000
    elif computer == 3:
        price = 50000
    else:
        print("Invalid Choice!!Try Again")
    quantity = int(input("\t\t\t\t\tenter number of quantity"))
    delivery = int(input("\t\t\t\t\tdelivery option: \n\t\t\t\t press 1 for:home delivery \n\t\t\t\t 2 for pickup"))
    if delivery == 1:
        charge = 100
    else:
        charge = 0
    packaging = int(input("""\t\t\t\t\tenter packaging option:
       \t\t\t\t\t 1 for plastic (Rs. 500)
       \t\t\t\t\t 2 for bag (Rs. 5000)
        \t\t\t\t\t3 for gift(Rs. 10000)
        \t\t\t\t\t4 for none
        """))
    if packaging==1:
        cost=500
    elif packaging==2:
        cost=5000
    elif packaging==3:
        cost=10000
    else:
        cost=0
    location = int(input("""\t\t\t\t\tselect your location
           \t\t\t\t\t 1 for kathmandu
           \t\t\t\t\t 2 for bkt
           \t\t\t\t\t 3 for ltp
            """))
    if location == 1:
        tax = 0.13
    else:
        tax=0
total_price = quantity * (price + cost + charge)
tax_amount = total_price * tax
grand_total = total_price + tax_amount
print(f"\t\t\t\t\ttotal quantity={quantity}")
print(f"\t\t\t\t\ttotal price={total_price}")
print(f"\t\t\t\t\ttax_amount={tax_amount}")
print(f"\t\t\t\t\ttotal price to be paid={grand_total}")
