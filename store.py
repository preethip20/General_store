# -*- coding: utf-8 -*-
import smtplib
from sys import exit
import texttable as tt
REGISTER_USER = {'preethi': 'admin123'}
RECEIPT_ELEMENTS = []
EMAIL_ADDRESS = 'preethi.p@centelon.com'
EMAIL_PASSWORD = 'Mahirocks@1'


class Store(object):
    """
    Command line program to create a Receipt generating Grocery Store
    """
    store_name = "Utsav General Store"
    cart_items = []
    cart_quantity = []
    cart_price = []
    user_name = "preethi"
    user_password = "admin123"
    sender = 'preethi.shettigar20@gmail.com'

    def __init__(self, name, password):
        """
        Initializes name and password
        """
        self.name = name
        self.password = password

    def joining(self):
        for i in range(0, len(self.cart_items)):
            for j in range(0, len(self.cart_quantity)):
                for k in range(0, len(self.cart_price)):
                    RECEIPT_ELEMENTS.append(self.cart_items[i])
                    RECEIPT_ELEMENTS.append(self.cart_quantity[j])
                    RECEIPT_ELEMENTS.append(self.cart_price[k])
                    k += 1
                    j += 1
                    i += 1
                    return '\t\t\t'.join(map(str, RECEIPT_ELEMENTS))
                break
            break

    def send_receipt(self, email_address, name):
        """
        Sends mail to the user
        """
        try:
            # res = list(map(lambda (i, j, k): i + j + k, zip(self.cart_items, self.cart_quantity, self.cart_price)))
            subject = "RECEIPT"
            msg = """	                RECEIPT
    --------------------------------------------------------------------------------------------
    Consumer Name: %s 
    --------------------------------------------------------------------------------------------
    PRODUCT                                 QUANTITY                                  PRICE
    --------------------------------------------------------------------------------------------
    %s
    --------------------------------------------------------------------------------------------
    CART TOTAL       =  %s  Rupees
    --------------------------------------------------------------------------------------------
    """ % (name.upper(), '\t\t\t\t\t\t'.join(map(str, RECEIPT_ELEMENTS)), self.print_total())
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            message = "Subject: {}\n\n{}".format(subject, msg)
            server.sendmail(EMAIL_ADDRESS, email_address, message)
            server.quit()
            print "-" * 40, "\nCHECK YOUR EMAIL! RECEIPT HAS BEEN SENT!\n", "-" * 40
        except smtplib.SMTPException:
            print "-" * 40, "\nFAILED TO SEND EMAIL! CHECK YOUR EMAIL ID!\n", "-" * 40

    def print_total(self):
        """
        print_total function will calculate the cart total and display the total
        """
        price_sum = 0
        for price in self.cart_price:
            price_sum = price_sum + price
        rupee_symbol = u"\u20B9"
        print "CART TOTAL = ", rupee_symbol, price_sum
        return price_sum

    def print_receipt(self, name):
        """
        print_receipt function is used to print the receipt for the consumer
        """
        print "\n\t\t\t\tReceipt"
        print "-" * 40, "\nConsumer Name:", name.upper(), "\n", "-" * 40
        for i in range(0, len(self.cart_items)):
            for j in range(0, len(self.cart_quantity)):
                for k in range(0, len(self.cart_price)):
                    RECEIPT_ELEMENTS.append(self.cart_items[i])
                    RECEIPT_ELEMENTS.append(self.cart_quantity[j])
                    RECEIPT_ELEMENTS.append(self.cart_price[k])
                    k += 1
                    j += 1
                    i += 1
                break
            break
        display_table = tt.Texttable()
        headings = ['Item Name', 'Quantity', 'Price']
        display_table.header(headings)
        for row in zip(self.cart_items, self.cart_quantity, self.cart_price):
            display_table.add_row(row)
        view_table = display_table.draw()
        print (view_table)
        self.print_total()
        print "-" * 40
        email_address = raw_input("Enter your email address to send receipt >")
        # print RECEIPT_ELEMENTS
        self.send_receipt(email_address, name)

    def category_choice_food_items(self, category_food_name, category_food_password):
        """
        Displays the list of food items to choose
        """
        print "-" * 40, "\nList of food items:\n", "-" * 40
        print "1) Bread\n2) Pizza\n3) Sandwich\n4) Burger\n5) Back to categories\n", "-" * 40
        try:
            item_choice = int(raw_input("Enter your choice:"))
            if item_choice == 5:
                self.display_categories(category_food_name, category_food_password)
            quantity = int(raw_input("Enter the quantity:"))
            if item_choice == 1:
                self.cart_items.append("Bread")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 15)
            elif item_choice == 2:
                self.cart_items.append("Pizza")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 90)
            elif item_choice == 3:
                self.cart_items.append("Sandwich")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 30)
            elif item_choice == 4:
                self.cart_items.append("Burger")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 30)
            else:
                print "-" * 40, "\nInvalid choice...Check your input again"
            print "-" * 40
        except ValueError:
            print "\n---PLEASE ENTER A VALID INTEGER---\n"

    def category_choice_drinks(self, category_drinks_name, category_drinks_password):
        """
        Displays the list of drinks to choose
        """
        print "-" * 40, "\nList of Drinks:\n", "-" * 40
        print "1) Frooti\n2) Sprite\n3) Fanta\n4) Zaffa\n5) Back to categories\n", "-" * 40
        try:
            item_choice = int(raw_input("Enter your choice:"))
            if item_choice == 5:
                self.display_categories(category_drinks_name, category_drinks_password)
            quantity = float(raw_input("Enter the quantity in litre:"))
            if item_choice == 1:
                self.cart_items.append("Frooti")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 25)
            elif item_choice == 2:
                self.cart_items.append("Sprite")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 25)
            elif item_choice == 3:
                self.cart_items.append("Fanta")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 27)
            elif item_choice == 4:
                self.cart_items.append("Zaffa")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 25)
            else:
                print "-" * 40, "\nInvalid choice...Check your input again"
            print "-" * 40
        except ValueError:
            print "\n---PLEASE ENTER A VALID INTEGER---\n"

    def category_choice_groceries(self, category_groceries_name, category_groceries_password):
        """
        Displays the list of groceries to choose
        """
        print "-" * 40, "\nList of Groceries:\n", "-" * 40
        print "1) Red Chilly\n2) Coriander seeds\n3) Sugar\n4) Salt\n5) Back to categories\n", "-" * 40
        try:
            item_choice = int(raw_input("Enter your choice:"))
            if item_choice == 5:
                self.display_categories(category_groceries_name, category_groceries_password)
            quantity = float(raw_input("Enter the quantity in kg:"))
            if item_choice == 1:
                self.cart_items.append("Red Chilly")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 85)
            elif item_choice == 2:
                self.cart_items.append("Coriander")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 60)
            elif item_choice == 3:
                self.cart_items.append("Sugar")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 45)
            elif item_choice == 4:
                self.cart_items.append("Salt")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 20)
            else:
                print "-" * 40, "\nInvalid choice...Check your input again"
            print "-" * 40
        except ValueError:
            print "\n---PLEASE ENTER A VALID INTEGER---\n"

    def category_choice_stationary(self, category_stationary_name, category_stationary_password):
        """
        Displays the list of stationaries to choose
        """
        print "-" * 40, "\nList of Stationaries:\n", "-" * 40
        print "1) Book\n2) Pen\n3) Pencil\n4) Eraser\n5) Back to categories\n", "-" * 40
        try:
            item_choice = int(raw_input("Enter your choice:"))
            if item_choice == 5:
                self.display_categories(category_stationary_name, category_stationary_password)
            quantity = int(raw_input("Enter the quantity:"))
            if item_choice == 1:
                self.cart_items.append("Book")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 45)
            elif item_choice == 2:
                self.cart_items.append("Pen")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 15)
            elif item_choice == 3:
                self.cart_items.append("Pencil")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 6)
            elif item_choice == 4:
                self.cart_items.append("Eraser")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 10)
            else:
                print "-" * 40, "\nInvalid choice...Check your input again"
            print "-" * 40
        except ValueError:
            print "\n---PLEASE ENTER A VALID INTEGER---\n"

    def category_choice_fashion(self, category_fashion_name, category_fashion_password):
        """
        Displays the list of fashion items to choose
        """
        print "-" * 40, "\nList of Fashion items:\n", "-" * 40
        print "1) T-Shirt\n2) Jeans\n3) Sweater\n4) Raincoat\n5) Back to categories\n", "-" * 40
        try:
            item_choice = int(raw_input("Enter your choice:"))
            if item_choice == 5:
                self.display_categories(category_fashion_name, category_fashion_password)
            quantity = int(raw_input("Enter the quantity:"))
            if item_choice == 1:
                self.cart_items.append("T-Shirt")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 250)
            elif item_choice == 2:
                self.cart_items.append("Jeans")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 500)
            elif item_choice == 3:
                self.cart_items.append("Sweater")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 450)
            elif item_choice == 4:
                self.cart_items.append("Raincoat")
                self.cart_quantity.append(quantity)
                self.cart_price.append(quantity * 900)
            else:
                print "-" * 40, "\nInvalid choice...Check your input again"
            print "-" * 40
        except ValueError:
            print "\n---PLEASE ENTER A VALID INTEGER---\n"

    def display_categories(self, name, d_password):
        """
        login function is used to display all the categories to the user
        """
        if name in REGISTER_USER.keys() and d_password == REGISTER_USER[name]:
            print "-" * 40, "\n\t\t\tWELCOME ", name.upper()
            my_choice = 1
            while my_choice:
                print "-" * 40, "\nCATEGORIES\n", "-" * 40
                print "1) Food Items\n2) Drinks\n3) Groceries\n4) Stationary\n5) Fashion\n6) Print Receipt\n7) Logout"
                print "-" * 40
                try:
                    category_choice = int(raw_input("Enter your choice:"))
                    if category_choice == 1:
                        self.category_choice_food_items(name, d_password)
                    elif category_choice == 2:
                        self.category_choice_drinks(name, d_password)
                    elif category_choice == 3:
                        self.category_choice_groceries(name, d_password)
                    elif category_choice == 4:
                        self.category_choice_stationary(name, d_password)
                    elif category_choice == 5:
                        self.category_choice_fashion(name, d_password)
                    elif category_choice == 6:
                        self.print_receipt(name)
                    elif category_choice == 7:
                        print "-" * 40, "\nYou have logged out successfully"
                        self.cart_items = []
                        self.cart_quantity = []
                        self.cart_price = []
                        break
                    else:
                        print "-" * 40, "\nInvalid choice...Check your input again\n", "-" * 40
                    print "\nDo you want to continue shopping?"
                    my_choice = int(raw_input("If YES press 1...If NO press 0 >"))
                    if my_choice == 0:
                        self.print_receipt(name)
                        exit(0)
                except ValueError:
                    print "\n---PLEASE ENTER A VALID INTEGER---\n"

    def login(self):
        """
        Takes username and password as input
        """
        print "-" * 40
        string = "LOGIN"
        print string.center(40)
        print "-" * 40
        user_name = raw_input("Enter the user name: ")
        pass_word = raw_input("Enter the password: ")
        return user_name, pass_word

    def register(self):
        """
        Register's a new user
        """
        print "-" * 40
        print "Do you want to register?\nIf YES press 'Y' if NO press any key"
        option = raw_input("Enter your choice >")
        if option == 'Y' or option == 'y':
            print "-" * 40
            string = "REGISTRATION"
            print string.center(40)
            print "-" * 40
            reg_username = raw_input("Enter the username >")
            reg_password = raw_input("Enter the password >")
            REGISTER_USER[reg_username] = reg_password
            print REGISTER_USER
            print "-" * 40, "\nUser registered successfully"
        else:
            pass

    def home_page(self):
        """
        This function is used to either log in or register a user
        """
        try:
            login_choice = 1
            while login_choice:
                print ""
                print "-" * 17, "LOGIN ", "-" * 15
                print "\t\t\tFor login press 'L'"
                print "-" * 15, "REGISTER", "-" * 15
                print "\t\tFor registration press 'R'"
                print "-" * 40
                user_choice = raw_input("Enter your choice >")
                if user_choice == 'L' or user_choice == 'l':
                    username, password = self.login()
                    self.validate_user(username, password)
                elif user_choice == 'R' or user_choice == 'r':
                    self.register()
                else:
                    print "-" * 40, "\nInvalid choice...check your input"
                print "-" * 40
                print "Do you want to continue?"
                login_choice = int(raw_input("If YES press 1...if NO press 0 >"))
        except ValueError:
            print "\n---INVALID INPUT GIVEN, RUN CODE AGAIN---"

    def validate_user(self, validate_username, validate_password):
        """
        Validates whether the username and password are valid or not
        """
        if validate_username in REGISTER_USER.keys() and validate_password == REGISTER_USER[validate_username]:
            print "-" * 40
            print "\tWELCOME TO ", self.store_name.upper()
            self.display_categories(validate_username, validate_password)
        else:
            print "-" * 40
            print "Invalid username or password"
            self.register()


"""
Outside the Store class
"""
store_object = Store(Store.user_name, Store.user_password)
store_object.home_page()



