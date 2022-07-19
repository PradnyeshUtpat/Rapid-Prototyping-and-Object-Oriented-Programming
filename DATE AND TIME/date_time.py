import datetime
print("\n Welcome to Time Zone")
while(1):
    print("\n\n1) Current date and time ")
    print("2) Current year ")
    print("3) Month of the year ")
    print("4) Week number of the year ")
    print("5) Which day of the week ")
    print("6) Day of the year ")
    print("7) Day of the month ")
    print("8) Day of the week ")
    print("9) Exit")
    choice= int(input("Enter your Choice: "))
    if(choice == 1):
        print("\nCurrent date and time: " , datetime.datetime.now())
    elif(choice == 2):
        print("\nCurrent year: ", datetime.date.today().strftime("%Y"))
    elif(choice == 3):
        print("\nMonth of the year: ", datetime.date.today().strftime("%B"))
    elif(choice == 4):
        print("\nWeek number of the year: ", datetime.date.today().strftime("%W"))
    elif(choice == 5):
        print("\nWhich day of the week: ", datetime.date.today().strftime("%w"))
    elif(choice == 6):
        print("\nDay of the year: ", datetime.date.today().strftime("%j"))
    elif(choice == 7):
        print("\nDay of the month : ", datetime.date.today().strftime("%d"))
    elif(choice == 8):
        print("\nDay of the week: ", datetime.date.today().strftime("%A"))
    elif(choice == 9):
        break
    else:
        print("Enter a valid choice")

print("Thank you for choosing your our services")