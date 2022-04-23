while True:
    i=input("input data inventory baru(ya/tidak)?")
    if i == "ya" or i == "Ya":
        file = open ("db-inventory.txt","a")
        print("*"*40)
        x = input("input nama perangkat :")
        y = input("input lokasi :")
        print("-"*40)
        file.write("Nama Perangkat : "+x+", \t lokasi : "+y+"\n")
        file.close()
    elif i == 'tidak' or i == 'Tidak':
        file = open("db-inventory.txt","r")
        print("*"*40)
        for item in file:
            item = item.strip()
            print(item)
        break