
import time
print("Written by Emin Ayyıldız")

Account_balance = 0

def check_account_balance():
    return Account_balance

def amount_deposited(amount):
    global Account_balance
    Account_balance += amount
    return "Amount Deposited: {}\nNew Amount: {}".format(amount, Account_balance)

def withdraw(amount):
    global Account_balance
    if amount > Account_balance:
        return "Insufficient Balance."
    else:
        Account_balance -= amount
        return "The amount you withdraw: {}\nNew Amount: {}".format(amount, Account_balance)

cards_in_system = [{'account_number': 1122334455, 'account_pin': 3131}, {'account_number': 20201706001, 'account_pin': 7412}]

def account_number_pin():
  account_number = int(input("Please enter your account number :"))
  account_pin = int(input("Please enter your account password  :"))
  for account in cards_in_system:
    if account['account_number'] == account_number and account['account_pin'] == account_pin:
            print("Logging into account")
            time.sleep(1.5)
            return True
  return False


while True:
  account_control = account_number_pin()
  if not account_control:
      print("Invalid card number or password....")
      continue
  while True:
    
    print("1. View account balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    your_choice = input("Your Choice: ")

    if your_choice == "1":
      print("Acount Balance : ", check_account_balance())
    elif your_choice == "2":
      amount = int(input("The amount you want to deposit : "))
      print(amount_deposited(amount))
    elif your_choice == "3":
      amount = int(input("The amount you want to withdraw : "))
      print(withdraw(amount))
    elif your_choice == "4" :
      break
    else:
      print("Invalid choice.")

