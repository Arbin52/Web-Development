from read import read_file
from datetime import datetime


def buyLaptop():
    print("Thank you for Purchasing With US")
    print("\n")
    print("----------------------------------------------------------------------")
    print("Please Enter your name and phone number")
    print("----------------------------------------------------------------------")
    print("\n")
    # Input validation for name
    while True:
        try:
            name = input("Enter Brand Name: ")
            if not name.isalpha():
                raise ValueError("Please provide a valid name !!")
            break
        except ValueError as e:
            print(e)
            print("\n")

    # Input validation for phone number
    while True:
        try:
            phone = input("Enter your Phone Number: ")
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Please provide a valid Phone Number !!")
            break
        except ValueError as e:
            print(e)
            print("\n")
    print("-----------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t    Price \t Quantity \t Processor \t Graphic Card")
    print("-----------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("solitude.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-----------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    purchased_laptops = []
    while True:
        valid_id = int(input("Please provide the ID of the product you want to Purchase:"))
        print("\n")

        # Valid ID
        while valid_id <= 0 or valid_id > len(read_file()):
            print("Please provide a valid Laptop ID !!")
            print("\n")
            valid_id = int(
                input("Please provide the ID of the laptop you want to Purchase: "))

        while True:
            try:
                user_quantity = input("quantity of laptop you wanna order: ")
                if not user_quantity.isdigit():
                    raise ValueError("Please provide quantity of laptop in number!")
                break
            except ValueError as z:
                print(z)
        print("\n")

        # Valid Quantity
        my_dict = read_file()
        get_quantity = my_dict[valid_id][3]

        # Update the text file
        my_dict[valid_id][3] = int(my_dict[valid_id][3]) + int(user_quantity)
        file = open("solitude.txt", "w")
        for values in my_dict.values():
            file.write(str(values[0])+"," + str(values[1])+"," + str(values[2]) +
                       "," + str(values[3])+"," + str(values[4])+"," + str(values[5]))
            file.write("\n")
        file.close()

        # Purchasing from manufacturer
        product_name = my_dict[valid_id][0]
        quantity = user_quantity
        Unit_price = my_dict[valid_id][2]
        item_price = my_dict[valid_id][2].replace("$", '')
        last_price = int(item_price)*int(quantity)
        purchased_laptops.append(
            [product_name, quantity, item_price, last_price])

        more_purchase = input("Do you want to Purchase more laptops? (Y/N): ")
        if more_purchase.lower() == 'n':
            break
        elif more_purchase.lower() == 'y':
            continue
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            more_purchase = input("Do you want to Purchase more laptops? (Y/N): ")
        if more_purchase.lower() == 'n':
            break
        elif more_purchase.lower() == 'y':
            continue
        else:
            print("Invalid input. Exiting loop.")
            break

    total = 0
    for i in purchased_laptops:
        total += int(i[3])
        VAT = 0.13*(total)
    final_total = total + VAT
    date_time = datetime.now()
    print("\n")
    print("\t \t \t \t WelCome TO Np Laptop Shop")
    print("\n")
    print("\t \t\t\t\   Basantapur, Kathmandu | Contact No: 98148484779 ")
    print("\n")
    print("----------------------------------------------------------------------------------------")
    print("Laptop Purchasing Details: ")
    print("----------------------------------------------------------------------------------------")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("----------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details are:")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Product Name \t\t Total Quantity \t Unit Price \t  Total")
    print("-----------------------------------------------------------------------------------------------------------")
    for i in purchased_laptops:
        print(i[0], "\t\t\t", i[1], "\t\t\t", i[2], "\t\t\t", "$", i[3])
    print("-----------------------------------------------------------------------------------------------------------")

    print("Vat Amount:",  VAT)
    print("Grand Total:" + str(final_total))
    print("Note: Vat Amount added to grand total")

    return name, phone, date_time, purchased_laptops, VAT, final_total


def sellLaptop():
    print("Thank you for Selling US")
    print("\n")
    print("---------------------------------------------------------------------")
    print("We will need your Name and Phone Number to print bill")
    print("---------------------------------------------------------------------")
    print("\n")
    # Input for valid name
    while True:
        try:
            name = input("Enter your Name: ")
            if not name.isalpha():
                raise ValueError("Please provide a Valid Name !!")
            break
        except ValueError as z:
            print(z)
            print("\n")
    # Input  for valid phone number
    while True:
        try:
            phone = input("Enter Your Phone Number: ")
            if not phone.isdigit() or len(phone) != 10:
                raise ValueError("Please provide a valid Phone Number !!")
            break
        except ValueError as e:
            print(e)
            print("\n")
    print("-----------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t      Brand \t   Price  \t Quantity  \t Processor  \t Graphic Card")
    print("-----------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("solitude.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-----------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

    laptop_sold = []

    while True:
        valid_id = int(input( "Please Provide the ID of the laptop you want to sell (Enter 9 to Exit): "))
        if valid_id == 9:
            break

        # Valid ID

        while valid_id <= 0 or valid_id > len(read_file()):
            print("Please Provide a valid Laptop ID !!")
            print("\n")
            valid_id = int(
                input("Please Provide the ID of the laptop you want to sell: "))

        user_quantity = int(
            input("Please Provide the number of quantity of the laptop you want to sell: "))
        print("\n")

        # Valid Quantity

        Mylap_dict = read_file()
        get_quantity = Mylap_dict[valid_id][3]
        while user_quantity <= 0 or user_quantity > int(get_quantity):
            print("Dear Admin, the quantity you are looking for is out of stock in our shop. Please look again in the Laptop screen")
            print("\n")
            user_quantity = int(
                input("Please Provide the Number of quantity of the Laptop you want to sell: "))
        print("\n")

        # Update the text file

        Mylap_dict[valid_id][3] = int(Mylap_dict[valid_id][3]) - int(user_quantity)

        file = open("solitude.txt", "w")

        for values in Mylap_dict.values():
            file.write(str(values[0])+"," + str(values[1])+"," + str(values[2]) +
                       "," + str(values[3])+"," + str(values[4])+"," + str(values[5]))
            file.write("," + str(values[1].split()[0]))
            file.write("\n")
        file.close()

        # getting user purchased items

        product_name = Mylap_dict[valid_id][0]
        quantity = user_quantity
        Unit_price = Mylap_dict[valid_id][2]
        item_price = Mylap_dict[valid_id][2].replace("$", '')
        last_price = int(item_price)*int(quantity)

        laptop_sold.append([product_name, quantity, item_price, last_price])

        sell_more = input("Do you want to sell more laptops? (Y/N): ")
        if sell_more.lower() == 'n':
            break
        elif sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Please enter 'Y' or 'N'.")
            sell_more = input("Do you want to Purchase more laptops? (Y/N): ")
        if sell_more.lower() == 'n':
            break
        elif sell_more.lower() == 'y':
            continue
        else:
            print("Invalid input. Exiting loop.")
            break

    date_time = datetime.now()
    # shipping_Cost = input(
    # "Dear Customer do you want your laptop to be shipped or not? (Y/N)")

    print("\n")
    print("\t \t \t \t Np Laptop Shop")
    print("\n")
    print("\t \t Basantapur, Kathmandu | Contact No: 9814848773 ")
    print("-----------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Laptop Selling Details: ")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Customer Name:" + str(name))
    print("Phone Number: " + str(phone))
    print("Date and Time: " + str(date_time))
    print("-----------------------------------------------------------------------------------------------------------")
    print("\n")
    print("Purchase Details are:")
    print("-----------------------------------------------------------------------------------------------------------")
    print("Product Name \t\t Total Quantity \t Unit Price \t Total")
    print("-----------------------------------------------------------------------------------------------------------")

    for i in laptop_sold:
        print(i[0], "\t\t\t", i[1], "\t\t\t", i[2], "\t\t\t", "$", i[3])
    print("-----------------------------------------------------------------------------------------------------------")

    total = 0
    shipping_Cost = 0
    shipping_choice = input(
        "Dear Customer do you want your laptop to be shipped?(Y/N): ")
    if shipping_choice.upper() == "Y":
        shipping_Cost = 200
        print("Note: Shipping Cost Added to Grand total")
        print("Shipping Cost:", shipping_Cost)

    for i in laptop_sold:
        total += int(i[3])
    last_total = total + shipping_Cost
    print("Total Amount:" + str(last_total))

    return name, phone, date_time, laptop_sold, shipping_Cost,last_total