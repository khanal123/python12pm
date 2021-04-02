def choice(ch):
    print("====================computerbazar===================")
    if ch == 'y' or ch == 'Y':
        def computer():
            cm = int(input("""\t\t\t\t\twhich computer do you want to buy press
            \t\t\t\t\t1. dell price(Rs.20000)
            \t\t\t\t\t2. mac price(Rs.50000)
            \t\t\t\t\t3. toshiba price (Rs.20000)
            """))
            if cm == 1:
                price = 20000
            elif cm == 2:
                price = 50000
            elif cm == 3:
                price = 50000
            else:
                print("Invalid Choice!!Try Again")
            return price

        def quantity():
            qt = int(input("\t\t\t\t\tenter number of quantity"))
            return qt

        def delivery():
            dv = int(input("\t\t\t\t\tdelivery option: \n\t\t\t\t press 1 for:home delivery \n\t\t\t\t 2 for pickup"))
            if dv == 1:
                charge = 100
            else:
                charge = 0
            return charge

        def packaging():
            pk = int(input("""\t\t\t\t\tenter packaging option:
            \t\t\t\t\t 1 for plastic (Rs. 500)
            \t\t\t\t\t 2 for bag (Rs. 5000)
            \t\t\t\t\t3 for gift(Rs. 10000)
            \t\t\t\t\t4 for none
            """))
            if pk == 1:
                cost = 500
            elif pk == 2:
                cost = 5000
            elif pk == 3:
                cost = 10000
            else:
                cost = 0
            return cost

        def location(l):
            l = int(input("""\t\t\t\t\tselect your location
            \t\t\t\t\t 1 for kathmandu
            \t\t\t\t\t 2 for bkt
            \t\t\t\t\t 3 for ltp
            """))
            if l == 1:
                tax = 0.13
            else:
                tax = 0
            return tax

        a=computer()
        b = quantity()
        c = delivery()
        d = packaging()
        e = location()
    total_price = b * (a + c + d)
    tax_amount = total_price * e
    grand_total = total_price + tax_amount
    print(f"\t\t\t\t\ttotal quantity={b}")
    print(f"\t\t\t\t\ttotal price={total_price}")
    print(f"\t\t\t\t\ttax_amount={tax_amount}")
    print(f"\t\t\t\t\ttotal price to be paid={grand_total}")
print("do you want to buy computer \n press y or Y if yes ")
ch = input("Enter your choice:")
choice(ch)
