def convertSalary():
    country2= input("Where do you want to migrate?").lower()
    salary= float(input("What is your salary in your home country? (Write after converting it to euros)"))

    canada_currency= salary*1.5
    usa_currency= salary*1.1
    cambodia_currency= salary*4500
    uk_currency= salary/0.8

    Canada_Average_Salary=56000 
    USA_Average_Salary=45000
    Cambodia_Average_Salary=7649856
    UK_Average_Salary=45423

    if(country2 == "Canada"):
        print("Your salary in Canada will be", canada_currency)
        if(canada_currency>Canada_Average_Salary):
            print("you will be rich in this country")
        if(canada_currency<Canada_Average_Salary):
            print("you will be poor in this country")

    if(country2 == "USA"):
        print("Your salary in USA will be", usa_currency)
        if(usa_currency>USA_Average_Salary):
            print("you will be rich in this country")
        if(usa_currency<USA_Average_Salary):
            print("you will be poor in this country")

    if(country2 == "Combodia"):
        print("Your salary in Cambodia will be", cambodia_currency)
        if(cambodia_currency>Cambodia_Average_Salary):
            print("You will be rich in this country")
        if(cambodia_currency<Cambodia_Average_Salary):
            print("You will be poor in this country")

    if(country2 == "UK"):
        print("Your salary in UK will be", uk_currency)
        if(uk_currency>UK_Average_Salary):
            print("You will be rich in this country")
        if(uk_currency<UK_Average_Salary):
            print("You will be poor in this country")

convertSalary()    



