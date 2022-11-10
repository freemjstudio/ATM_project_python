import random

account_object_list = []
FILE = "data.txt"

class Account:
    def __init__(self, account_number, name, balance, password, email):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.password = password
        self.email = email

    def print_account(self):
        print("-------------- User Information --------------")
        print("  Name: ",self.name)
        print("  Account Number :", self.account_number)
        print("  Balance: $", self.balance)
        print("-----------------------------------------------")

    def get_account_info(self):
        return self.account_number, self.name, self.balance

    def check_password(self):
        print("Enter the PIN : ")
        input_password = input()
        if input_password == self.password:
            return True
        else:
            return False # 회원정보 불일치

# Function
def register(): # 회원 가입
    print("Enter name: ")
    input_name = input()
    print("Enter email number: ")
    input_email = input()
    print("Enter PIN: ")
    input_password = input()

    new_account_num = ""
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999999)
    num3 = random.randint(0, 99999)
    num1 = str(num1).zfill(3)
    num2 = str(num2).zfill(6)
    num3 = str(num3).zfill(5)
    new_account_num = num1+ '-' +num2+'-'+num3

    new_account = Account(new_account_num, input_name, 0, input_password, input_email) # balance = 0
    account_object_list.append(new_account)
    new_account.print_account()
    save_data()
    print("Successfully Registered! ")

def check_vaild_account(user_account):
    for account_object in account_object_list:
        new_account_number = account_object.account_number.replace('-','')
        if user_account == account_object.account_number:
            return account_object
        elif user_account == new_account_number:
            return account_object
    return None

def read_data():
    print("[Loading] System is reading the data...")
    try:
        file = open(FILE, 'r')
        while True:
            line = file.readline()
            if not line:
                break
            account_number, name, balance, password, email = line.split()
            account_object_list.append(Account(account_number, name, int(balance), password, email))
        file.close()
    except Exception as error:
        print("[Error] There's no data.txt file. ")
        print(error)

def save_data():
    f = open(FILE, 'w')
    for data in account_object_list:
        data_str = data.account_number+' '+data.name+' '+str(data.balance)+' '+data.password+' '+data.email+' \n'
        f.write(data_str)
    f.close()

def deposit(user_data):
    print("How much would you like to deposit? ")
    input_deposit = input()
    if input_deposit.isdigit():
        user_data.balance += int(input_deposit)
        user_data.print_account()
    else:
        print("[Error] Enter valid integer!")

def withdraw(user_data):
    print("How much would you like to withdraw? ")
    input_withdraw = input()
    if input_withdraw.isdigit():
        if user_data.balance >= int(input_withdraw):
            user_data.balance -= int(input_withdraw)
            user_data.print_account()
        else:
            print("[Error] Insufficient balance in your account! ")
    else:
        print("[Error] Enter valid integer!")

def check_valid_user(input_user, input_email):
    for account_object in account_object_list:
        if input_user == account_object.name and input_email == account_object.email:
            return account_object
    return None

def find_account_number():
    print("Enter user name:")
    input_name = input()
    print("Enter user email:")
    input_email = input()
    account_object = check_valid_user(input_name, input_email)
    if account_object != None:
        print(input_name,"'s account number is")
        print(account_object.account_number)
        print("Thank you")
    else:
        print("[Error] There's no user information")
    return None

def change_password():
    print("Enter account")
    input_account = input()
    print("Enter user name")
    input_name = input()
    print("Enter user email")
    input_email = input()
    account_object = check_vaild_account(input_account)
    account_object2 = check_valid_user(input_name, input_email)
    if account_object2 != None and account_object != None:
        while True:
            print("Enter new PIN:")
            input_password = input()
            print("Enter the new PIN number again:")
            input_password_check = input()

            if input_password_check == input_password:
                account_object.password = input_password
                save_data()
                print("PIN number is successfully changed")
                break
            else:
                print("[Error] PIN number doesn't match ! ")
    else:
        print("[Error] There's no user matched with the input data ! ")
        return

# View
def default_view():
    thank_you_ascii = """
              ________                __                       
         /_  __/ /_  ____ _____  / /__   __  ______  __  __
          / / / __ \/ __ `/ __ \/ //_/  / / / / __ \/ / / /
         / / / / / / /_/ / / / / ,<    / /_/ / /_/ / /_/ / 
        /_/ /_/ /_/\__,_/_/ /_/_/|_|   \__, /\____/\__,_/  
                                      /____/               
            
            Developed by Minjee woo @freemjstudio GitHub
            """
    read_data()
    while True:
        print("--------------- ATM Service ---------------")
        print(" 1. Enter Account")  # 계좌번호 입력하기
        print(" 2. Register ")  # 회원가입
        print(" 3. Find Account")
        print(" 4. Can't find PIN number")
        print(" 0. Exit")
        print("Choose the option: ", end=" ")
        op = input()
        if op == '1':
            print("Enter the account number")
            user_input_account = input()
            user_data = check_vaild_account(user_input_account)

            if user_data != None:
                if user_data.check_password():
                    menu_view(user_data)
                else:
                    print("[Error] Wrong PIN number")
            else:
                print("[Error] Wrong Account number")
        elif op == '2':
            register()
        elif op == '3':
            find_account_number()
        elif op == '4':
            change_password()
        elif op == '0':
            save_data()
            print(thank_you_ascii)
            exit()
        else:
            print("[Error] Enter right number")

def menu_view(user_data):
    print("--------------- MENU ----------------")
    print("| 1. Check balance                  |")
    print("| 2. Deposit                        |")
    print("| 3. Withdraw                       |")
    print("| 0. Exit                           |")
    print("-------------------------------------")
    print("Choose the option")
    op = input()
    if op == '0':
        return  # 이전 화면으로 돌아가기
    elif op == '1':  # Check balance
        user_data.print_account()
    elif op == '2':  # Deposit
        deposit(user_data)
    elif op == '3':
        withdraw(user_data)

def main():
    atm_ascii = """ 
    ___  ________  ___   _____                 _         
   /   |/_  __/  |/  /  / ___/___  ______   __(_)_______ 
  / /| | / / / /|_/ /   \__ \/ _ \/ ___/ | / / / ___/ _ \ 
 / ___ |/ / / /  / /   ___/ /  __/ /   | |/ / / /__/  __/
/_/  |_/_/ /_/  /_/   /____/\___/_/    |___/_/\___/\___/ 
                                                         
  Developed by Minjee woo, GitHub @freemjstudio 
  
    """
    print(atm_ascii)
    default_view()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()