print("====================computerbazar===================")
class computer:
    def choose_computer(self):
        self.computer = int(input("""\t\t\t\t\twhich computer do you want to buy press
                   \t\t\t\t\t1. dell price(Rs.20000)
                   \t\t\t\t\t2. mac price(Rs.50000)
                   \t\t\t\t\t3. toshiba price (Rs.20000)
                   """))
        if self.computer == 1:
            self.price = 20000
        elif self.computer == 2:
            self.price = 50000
        elif self.computer == 3:
            self.price = 20000
        else:
            print("Invalid choice!!! Try Again")
        return self.price

    def quantity(self):
        self.qt = int(input("\t\t\t\t\tenter number of quantity"))
        return self.qt

    def delivery(self):
        self.dv = int(input("\t\t\t\t\tdelivery option: \n\t\t\t\t press 1 for:home delivery \n\t\t\t\t 2 for pickup"))
        if self.dv == 1:
            self.charge = 100
        else:
            self.charge = 0
        return self.charge

    def packaging(self):
        self.pack = int(input("""\t\t\t\t\tenter packaging option:
                       \t\t\t\t\t 1 for plastic (Rs. 500)
                       \t\t\t\t\t 2 for bag (Rs. 5000)
                        \t\t\t\t\t3 for gift(Rs. 10000)
                        \t\t\t\t\t4 for none
                        """))
        if self.pack == 1:
            self.cost = 500
        elif self.pack == 2:
            self.cost = 5000
        elif self.pack == 3:
            self.cost = 10000
        else:
            self.cost = 0
        return self.cost
    def location(self):
        self.l = int(input("""\t\t\t\t\tselect your location
                   \t\t\t\t\t 1 for kathmandu
                   \t\t\t\t\t 2 for bkt
                   \t\t\t\t\t 3 for ltp
                    """))
        if self.l == 1:
            self.tax = 0.13
        else:
            self.tax = 0
        return self.tax
    def total(self):
        self.total_price = self.qt * (self.price + self.charge + self.cost)
        self.tax_amount = self.total_price * self.tax
        self.grand_total = self.total_price + self.tax_amount
        print(f"\t\t\t\t\ttotal quantity={self.qt}")
        print(f"\t\t\t\t\ttotal price={self.total_price}")
        print(f"\t\t\t\t\ttax_amount={self.tax_amount}")
        print(f"\t\t\t\t\ttotal price to be paid={self.grand_total}")
print("do you want to buy computer \n press y or Y if yes ")
choice = input("Enter your choice")
if choice=='y' or choice=='Y':
    obj=computer()
    obj.choose_computer()
    obj.quantity()
    obj.delivery()
    obj.packaging()
    obj.location()
    obj.total()