def read_file():
    file = open("solitude.txt","r")
    laptop_sn= 1
    MyLap_dict = {}
    for line in file:
        line = line.replace("\n","")
        MyLap_dict[laptop_sn] = (line.split(","))
        laptop_sn += 1
    file.close()
    return MyLap_dict