database_balance = {}


class Budget:
    def __init__(self, amount, categories):
        self.amount = amount
        self.categories = categories

    def deposit(self, amount, balance):
        balance += amount
        return balance

    def withdraw(self, user, amount, balance):
        balance -= amount
        return balance

    def balance(self, database_balance):
        for categories, balance in database_balance.items():
            print(categories, balance)

    def transfer(self, database_balance, send, amount, receive):
        value1 = database_balance[send]
        value2 = database_balance[receive]

        database_balance[send] = int(value1) - amount
        database_balance[receive] = int(value2) + amount

        return database_balance


def init():
    print("This is a Pseudo Budget App")
    menu()


def menu():
    try:
        user = input(
            '\nEnter ===\n"d" To Deposit,\n"w" To Withdraw,\n "c" To Check Balance,\n "t" To Transfer,\n "cb"To create a new budget,\n "q"To quit \n')
    except:
        print('Invalid input')
        menu()

    if user == 'cb':
        new_budget()
    elif user == 'd':
        dep()
    elif user == 'w':
        witdraw()
    elif user == 'c':
        balance()
    elif user == 5:
        tfare()
    else:
        print('Invalid input\n')
        menu()


def new_budget():
    print("\n=== ***Creating a Budget**** ===\n")

    budget_title = input("Enter budget name \n")
    try:
        amount = int(input("Enter your budget amount \n$"))
    except:
        print('\nInvalid input')
        new_budget()
    database[budget_title] = amount
    print('')
    print(f'Budget {budget_title} was setup with ${amount}')
    menu()


def witdraw():
    print("=== ****Withdraw budget**** ===\n")
    print('**** Available Budget ****')

    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input(
        '\nPress (1) To continue with your witdraw transaction\nPress (2) To stop witdraw transaction\n'))
    if pick == 1:
        user = input("\n**** Select one of budget(s) aforementioned ****\n")
        if user in database:
            print('Note: You can not witdraw all your budget, at least $1 must remain.')
            amt = int(input("Enter amount \n$"))
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.witdraw(user, amt, balance)
                database[user] = new_balance
                print(
                    f"${amt} has been debited from Budget-{user}\nBudget amount remaining ${new_balance}")
                menu()

            else:
                pick = int(input(
                    f'\nBudget {user} is insufficient of the ${amt} required\nThe actual balance {database[user]}\n\nPress (1) To dep to the budget\nPress (2) To choose the right budget\n'))
                if pick == 1:
                    amt = int(input("Enter amount \n$"))
                    balance = int(database[user])
                    new_balance = Budget.dep(amt, balance)
                    database[user] = new_balance
                    print('')
                    print(f"Budgets {user} has been credited with ${amt}\n")
                    witdraw()

                elif pick == 2:
                    witdraw()
                else:
                    print('Invalid option\n')
                    witdraw()
        else:
          pick = int(input(
              f'\n****  Budget {user} does not exist! ****\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
          if pick == 1:
              new_budget()
          elif pick == 2:
              witdraw()
          elif pick == 3:
              print('')
              menu()
          else:
              print('Invalid option\n')
              witdraw()
    elif pick == 2:
        print('\nYou have terminated the witdraw transaction ')
        menu()
    else:
        print('\nInvalid option')
        witdraw()


def dep():
    print("**** Deposit into a budget ****\n")
    print('**** Available Budgets ****')
    for key, value in database.items():
        print(f"-  {key}")

    pick = int(input(
        '\nPress (1) To continue with your dep transaction\nPress (2) To stop dep transaction\n'))
    if pick == 1:
        user = input("Select a budget \n")
        if user in database:
            amt = int(input("Enter amount \n$"))
            balance = int(database[user])
            new_balance = Budget.dep(amt, balance)
            database[user] = new_balance
            print(
                f'\nBudget {user} is credited with ${amt}\nTotal Budget amount is now ${new_balance}')
            menu()

        else:
            print('')
            pick = int(input(
                f'Budget {user} does not exist!\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
            if pick == 1:
                new_budget()
            elif pick == 2:
                dep()
            elif pick == 3:
                menu()
            else:
                print('Invalid option\n')
                dep()

    elif pick == 2:
        print('\nYou terminated the dep transaction')
        menu()
    else:
        print('\nInvalid option')
        dep()


def balance():
    print("*** Getting Your Budget Balance***\n")
    check_bal = Budget.balance(database)
    if (check_bal == None):
        print('')
        menu()
    else:
        print(f'${check_bal}')
        menu()


def tfare():
    print('**** Available and Valid Budgets ****')
    for key, value in database.items():
        print(key)
        print('')
    print("**** Transfer Operations ****")
    print('Note: You can not witdraw all your budget, at least $1 must remain.\n')
    from_budget = input("Enter the buget you are transfering from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to tfare \n$"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds \n")
            if to_budget in database:
                db = Budget.tfare(database, from_budget,
                                  from_amount, to_budget)
                print("")
                print(
                    f"You transfered ${from_amount} from {from_budget} to {to_budget} ")
                for key, value in db.items():
                    print(key, value)
                menu()
            else:
                print(
                    f'\n{from_budget} Budget does not exist, please choose from the valid budget below\n')
                tfare()
        else:
            print(
                f'You do not have such amount-${from_amount} in {from_budget} budget')
            tfare()
    else:
        print(f'Budget {from_budget} does not exist\n')

        tfare()


def quit():
    try:
        pick = int(input(
            'Do you want to quit?\nPress (1) to quit\nPress (2) to continue\n'))
    except:
        print('Invalid input\n')
        quit()

    if pick == 1:
        print("\nWe hope you had a good budgeting experience, bye for now.")
        quit()
    elif pick == 2:
        menu()
    else:
        print('Invalid input\n')
        quit()


init()
