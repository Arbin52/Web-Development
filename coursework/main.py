from operation import buyLaptop
from operation import sellLaptop
from write import W_laptoppurchase, W_laptopsell

def displayLaptops():
    print("-----------------------------------------------------------------------------------------------------------")
    print("S.N. \t Name \t\t     Brand \t \t   Price  \t Quantity  \t Processor \t Graphic Card")
    print("-----------------------------------------------------------------------------------------------------------")
    a = 1
    file = open("solitude.txt", "r")
    for line in file:
        print(a, "\t" + line.replace(",", "\t"))
        a = a + 1
    print("-----------------------------------------------------------------------------------------------------------")
    file.close()
    print("\n")

print("\n")
print("---------------------------------------------------------------------------------------------------------------")
print("\t \t \t \t Welcome to Np Laptop Shop")
print("---------------------------------------------------------------------------------------------------------------")
print("\t \t \t Address: Basantapur, Kathmandu | Contact: 987456321")
print("---------------------------------------------------------------------------------------------------------------")
print("\n")

continueLoop = True
while continueLoop:
    print("\n")
    print("Press 1 to Purchase from manufacture")
    print("Press 2 to Sell to customer")
    print("Press 3 to Display available laptops")
    print("Press 4 to Exit")
    print("\n")
    print("-----------------------------------------------------------------------------------------------------------")
    try:
        userinput = int(input("Press 1,2,3 or 4 :"))
        if userinput == 1:
            name,phone,date_time,purchased_laptops,VAT,final_total = buyLaptop()
            W_laptoppurchase(name,phone,date_time,purchased_laptops,VAT,final_total)

        elif userinput == 2:
            name,phone,date_time,laptop_sold,cost_of_shipping,final_total = sellLaptop()
            W_laptopsell(name,phone,date_time,laptop_sold,cost_of_shipping,final_total)

        elif userinput == 3:
            displayLaptops()

        elif userinput == 4:
            continueLoop = False
            print("Thank you for Visiting US")

        else:
            print("Enter correct option. Try Again")
    except ValueError:
        print("Invalid input. Please Enter a number from 1, 2, 3 or 4.")
