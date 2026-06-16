class BankAccount:
    bank_name = "Vietcombank"
    transaction_fee = 2000

    def __init__(self, account_number, account_name):
        self.account_number = account_number
        self.__account_name = account_name.strip().upper()
        self.__balance = 0

    @property
    def balance(self):
        return self.__balance

    @property
    def account_name(self):
        return self.__account_name

    @account_name.setter
    def account_name(self, value):
        if not value or value.strip() == "":
            print("Tên tài khoản không được để trống")
        else:
            self.__account_name = value.strip().upper()

    @staticmethod
    def validate_account_number(account_number):
        return account_number.isdigit() and len(account_number) == 10

    @classmethod
    def update_transaction_fee(cls, new_fee):
        if new_fee < 0:
            print("Phí giao dịch không được âm")
            return False
        cls.transaction_fee = new_fee
        return True

    def deposit(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
        else:
            self.__balance += amount
            print(f"Nạp tiền thành công: +{amount:,} VND")

    def withdraw(self, amount):
        if amount <= 0:
            print("Số tiền giao dịch phải lớn hơn 0")
        elif self.__balance < (amount + self.transaction_fee):
            print("Giao dịch thất bại. Số dư không đủ để thanh toán số tiền và phí giao dịch")
        else:
            self.__balance -= (amount + self.transaction_fee)
            print(f"Rút tiền thành công: -{amount:,} VND")
            print(f"Phí giao dịch: {self.transaction_fee:,} VND")

    def display_info(self):
        print(f"\n--- THÔNG TIN TÀI KHOẢN ---")
        print(f"Ngân hàng: {self.bank_name}")
        print(f"Số tài khoản: {self.account_number}")
        print(f"Tên chủ tài khoản: {self.__account_name}")
        print(f"Số dư hiện tại: {self.__balance:,} VND")
        print(f"Phí giao dịch: {self.transaction_fee:,} VND")

def main():
    current_account = None
    
    while True:
        print("""

===== VIETCOMBANK DIGIBANK SIMULATOR =====
1. Mở tài khoản mới                      
2. Xem thông tin tài khoản
3. Giao dịch Nạp / Rút tiền
4. Cập nhật Tên chủ tài khoản
5. Đổi phí giao dịch hệ thống
6. Thoát chương trình                     
------------------------------------------""")
        choice = input("Chọn chức năng (1-6): ")

        match choice:
            case '1':
                acc_num = input("Nhập số tài khoản 10 chữ số: ")
                if BankAccount.validate_account_number(acc_num):
                    name = input("Nhập tên chủ tài khoản: ")
                    current_account = BankAccount(acc_num, name)
                    print("Mở tài khoản thành công!")
                else:
                    print("Số tài khoản không hợp lệ! Số tài khoản phải gồm đúng 10 chữ số.")

            case '2':
                if not current_account:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản (Chức năng 1) trước.")
                else:
                    current_account.display_info()

            case '3':
                if not current_account:
                    print("Hệ thống chưa có thông tin tài khoản. Vui lòng mở tài khoản (Chức năng 1) trước.")
                else:
                    print("""--- GIAO DỊCH NẠP / RÚT TIỀN ---
                    1. Nạp tiền
                    2. Rút tiền  
                    """)
                   
                    minichoice = input("Chọn loại giao dịch (1-2): ")
                    try:
                        amount = int(input("Nhập số tiền giao dịch: "))
                        match minichoice:
                            case '1':
                                print(f"Số dư mới: {current_account.balance:,} VND")
                                current_account.deposit(amount)
                            case '2':
                                current_account.withdraw(amount)
                                print(f"Số dư mới: {current_account.balance:,} VND")
                            case _:
                                print("Loại giao dịch không hợp lệ.")
                      
                            
                    except ValueError:
                        print("Số tiền phải là số nguyên.")

            case '4':
                if not current_account:
                    print(" Vui lòng mở tài khoản ")
                else:
                    new_name = input("Nhập tên mới: ")
                    current_account.account_name = new_name
                    print(f"Tên mới: {current_account.account_name}")

            case '5':
                print(f"Phí giao dịch hiện tại: {BankAccount.transaction_fee:,} VND")
                try:
                    new_fee = int(input("Nhập phí giao dịch mới: "))
                    if BankAccount.update_transaction_fee(new_fee):
                        print(f"Đã cập nhật phí giao dịch toàn hệ thống thành {BankAccount.transaction_fee:,} VND")
                except ValueError:
                    print("Phí giao dịch phải là số nguyên.")

            case '6':
                print("Cảm ơn bạn đã sử dụng Vietcombank Digibank!")
                break
            
            case _:
                print("Chức năng không hợp lệ, vui lòng chọn từ 1-6.")

if __name__ == "__main__":
    main()