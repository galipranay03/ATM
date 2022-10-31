#ATM simulater

print('Bank of world ')
restart = 'Y'
chances = 3
amount = 10000

while chances >= 0:
    pin = int(input("Enter your 4 digit pin: "))
    if pin == 5256:
        print("Your entered correct pin.")
        while restart not in ('n','N','NO','no'):
            print('Press 1 to check your balance: ')
            print('Press 2 for withdrawl cash: ')
            print('press 3 for deposite cash')
            print('press 4 to return card:')
            option = int(input("Enter your Options(1,2,3,4):"))
            if option == 1:
                print('Your account Balance is:', amount)
                restart = input("Would you like to go back?")
                if restart in ('n','N','NO','no'):
                    print('ThankYou')
                    break
            elif option == 2:
                withdrawl = int(input("Enter your amount(100,500,2000):"))
                if withdrawl in (100,500,2000):
                    totalbal = amount-withdrawl
                    print("You account balance is:",totalbal)
                    restart = input("Would you like to go back?")
                    if restart in ('n', 'N', 'NO', 'no'):
                        print('ThankYou')
                        break
                elif withdrawl != (10,50,200,1000):
                    print("Invalid amount Re-Try:")
                    restart = 'Y'
            elif option == 3:
                addcash = (int(input("Enter your deposite money(100,500,2000):")))
                if addcash in (100,500,2000):
                    addcash = addcash+amount
                    print("You account balance is:", addcash)
                    restart = input("Would you like to go back?")
                    if restart in ('n', 'N', 'NO', 'no'):
                        print('ThankYou')
                        break
            elif option == 4:
                print("Please wait Until your card return..")
                print("ThankYou for your Service")
                break
            else:
                print("please enter a correct number(1,2,3,4):")
                restart = "Y"
    elif pin != 5256:
        print("Invaild Pin")
        chances = chances - 1
        if chances == 0:
            print("no more tries")
        break
