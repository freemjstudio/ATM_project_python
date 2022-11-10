import random
import sys
account_object_list = []

class Account:
    def __init__(self, account_number, name, balance, password):
        self.account_number = account_number
        self.name = name
        self.balance = balance
        self.password = password

    def print_account(self):
        print("-------------- User Information --------------")
        print("Name: ",self.name)
        print("Account Number :", self.account_number)
        print("Balance: $", self.balance)

    def get_account_info(self):
        return self.account_number, self.name, self.balance

    def check_password(self):
        print("Enter the PIN : ")
        input_password = input()
        if input_password == self.password:
            return True
        else:
            return False # 회원정보 불일치

def register(): # 회원 가입
    print("Enter name: ")
    input_name = input()
    print("Enter PIN: ")
    input_password = input()

    new_account_num = ""
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999999)
    num3 = random.randint(0, 99999)
    num1 = str(num1).zfill(3)
    num2 = str(num2).zfill(6)
    num3 = str(num3).zfill(5)
    new_account_num = str(num1)+ '-' +num2+'-'+num3

    new_account = Account(new_account_num, input_name, 0, input_password) # balance = 0
    account_object_list.append(new_account)
    new_account.print_account()
    print("Successfully Registered! ")


def check_vaild_account(user_account):
    for account_object in account_object_list:
        if user_account == account_object.account_number:
            return account_object
    return None


def default_view():
    
    while True:
        print("--------------- ATM Service ---------------")
        print(" 1. Enter Account")  # 계좌번호 입력하기
        print(" 2. Register ")  # 회원가입
        print(" 0. Exit")
        print("Choose the option: ", end=" ")
        choice = input()
        if choice == '1':
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
        elif choice == '2':
            register()
        elif choice == '0':
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
        print("How much would you like to deposit? ")
        input_deposit = input()
        if input_deposit.isdigit():
                user_data.balance += int(input_deposit)
                user_data.print_account()
        else:
            print("[Error] Enter valid integer!")
    elif op == 3:
        print("How much would you like to withdraw? ")
        input_withdraw = input()
        if input_withdraw.isdigit():
            user_data.balance -= int(input_withdraw)
            user_data.print_account()
        else:
            print("[Error] Enter valid integer!")

def main():
    atm_ascii = """ 
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |      __      | || |  _________   | || | ____    ____ | |
| |     /  \     | || | |  _   _  |  | || ||_   \  /   _|| |
| |    / /\ \    | || | |_/ | | \_|  | || |  |   \/   |  | |
| |   / ____ \   | || |     | |      | || |  | |\  /| |  | |
| | _/ /    \ \_ | || |    _| |_     | || | _| |_\/_| |_ | |
| ||____|  |____|| || |   |_____|    | || ||_____||_____|| |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
    """
    print(atm_ascii)
    default_view()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()