import mysql.connector as c
con = c.connect(host = 'localhost',
                user = 'root',
                passwd = 'Abhi@2002',
                database = 'bob')

cursor = con.cursor()
while True:
    choice = int(input("for open account press 9 for diposit press 1 & for withdrawl press 2 & for delete account press 0 "))
    # open account
    if choice==9:

        Name = input("enter costumer name ")
        Father_Name = input("enter costumer father name ")
        Date_of_Birth = input("enter date of birth ")
        Mobile_no = input("enter costumer mobile no ")
        Account_Type = input("enter account type ")
        Deposit_Money = int(input("enter deposit money "))
        Withdrawl_Money = int(input("enter withdraw money "))

        query = "insert into costumer values('{}','{}',{},'{}','{}',{},{})".format(Name,Father_Name,Date_of_Birth,Mobile_no,Account_Type,Deposit_Money,Withdrawl_Money)
        cursor.execute(query)
        con.commit()

        print("account open successfully")

        press = int(input('press 0 to stop the entry & press any no. to more entry '))
        if press == 0:
            break

    # deposit money
    elif choice==1:

        Deposit_Money = int(input("enter your ammount for deposit "))
        Name = input("enter account holder name ")

        query = "update costumer set Deposit_Money = {} where Name = '{}'".format(Deposit_Money,Name)
        cursor.execute(query)
        con.commit()

        print("money deposit successfully")

        press = int(input('press 0 to stop the entry & press any no. to more entry '))
        if press == 0:
            break

    #     withdraw money
    elif choice==2:

        Withdrawl_Money = int(input("enter your ammount for withdrawl "))
        Name = input("enter account holder name ")

        query = "update costumer set Withdrawl_Money = {} where Name = '{}'".format(Withdrawl_Money,Name)
        cursor.execute(query)
        con.commit()

        print("money withdraw successfully")

        press = int(input('press 0 to stop the entry & press any no. to more entry '))
        if press == 0:
            break

    #     delete account
    elif choice==0:

        Name = input("enter account holder name ")

        query = "delete from costumer where Name = '{}'".format(Name)
        cursor.execute(query)
        con.commit()

        print("account deleted successfully")

        press = int(input('press 0 to stop the entry & press any no. to more entry '))
        if press==0:
            break