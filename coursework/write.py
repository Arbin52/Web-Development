def W_laptopsell(name, phone, date_time, laptop_sold, shipping_Cost, final_total):
    with open(str(name) + str(phone) + ".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t \t\t WelCome To Np Laptop Shop")
        file.write("\n")
        file.write("\t \t \t Basantapur, Kathmandu | Contact No: 9814848773 ")
        file.write("\n\n")
        file.write(
            "---------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("\t\t\t Laptop Selling Details: ")
        file.write("\n")
        file.write("\t\t\t----------------------\n")
        file.write("\t\t\t Customer Name:" + str(name))
        file.write("\n")
        file.write("\t\t\t Customer's Phone Number: " + str(phone))
        file.write("\n")
        file.write("\t\t\t Date and Time: " + str(date_time))
        file.write("\n")
        file.write(
            "\t\t\t---------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("\t\t\t Laptop Buying Details:")
        file.write("\n")
        file.write(
            "\t\t\t-------------------------------------------------------------------------------------------------\n")
        file.write("\t\t\t Laptop Name \t\t  Quantity \t\t Unit Price \t\t Total")
        file.write("\n")
        file.write(
            "-------------------------------------------------------------------------------------------------\n")
        for i in laptop_sold:
            file.write(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" +
                       str(i[2]) + "\t\t\t" + "$" + str(i[3])+"\n")
        file.write(
            "\t\t--------------------------------------------------------------------------------------------------\n")
        file.write("\n")
        if shipping_Cost == 200:
            file.write("Shipping Cost:" + "" + str(shipping_Cost) + "\n")
            file.write("\n")
            file.write(" Total Amount: $" + str(final_total) + "\t\t\t"
                       "[Note: Shipping Amount added to total amount]" + "\n")
            file.write("\n")
        else:
            file.write("Total Amount: $" + str(final_total))


def W_laptoppurchase(name, phone, date_time, laptop_bought, VAT, final_total):
    with open(str(name) + str(phone) + ".txt", "w")as file:
        file.write("\n")
        file.write("\t \t \t \t\t Welcome To Np Laptop Shop")
        file.write("\n")
        file.write("\t \t\t Basatapur, Kathmandu | Phone No: 9814848789")
        file.write("\n")
        file.write(
            "\t\t---------------------------------------------------------------------------------------\n")
        file.write("\t\t Laptop Details: ")
        file.write("\n")
        file.write("\t\t--------------------------\n")
        file.write("\t\t Company Name:" + str(name))
        file.write("\n")
        file.write("\t\t Phone Number: " + str(phone))
        file.write("\n")
        file.write("\t\t Date and Time: " + str(date_time))
        file.write("\n")
        file.write(
            "\t\t ---------------------------------------------------------------------------------------\n")
        file.write("\n")
        file.write("\t\t Laptop Buying Details:")
        file.write("\n")
        file.write(
            "\t\t---------------------------------------------------------------------------------------------------\n")
        file.write("\t\t Laptop Name \t\t Quantity \t\t Unit Price \t\t Total")
        file.write("\n")
        file.write(
            "\t\t----------------------------------------------------------------------------------------------------\n")
        for i in laptop_bought:
            file.write(str(i[0]) + "\t\t\t" + str(i[1]) + "\t\t\t" +
                       str(i[2]) + "\t\t\t" + "$" + str(i[3])+"\n")
        file.write(
            "\t\t-------------------------------------------------------------------------------------------------\n")
        file.write("\n")
        if VAT:
            file.write("\t\t Vat Amount:" + "" + str(VAT) + "\n")
            file.write("\n")
            file.write("\t\t Total Amount: $" + str(final_total) + "\n")
            file.write("\n")
            file.write("\t\t Note: Vat Amount added to total amount" + "\n")
            file.write("\n")
        else:
            file.write("Total Amount: $" + str(final_total))