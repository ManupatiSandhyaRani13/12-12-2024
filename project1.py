class Bank:
    bal=100000
    def deposit(self):
        amt=int(input("enter the deposit amount:"))
        if amt>=100 and amt<=50000 and amt%100==0:
            self.bal+=amt
            print('Total balnce is ',self.bal)
        else:
            print('minimum deposit should be 100 ,maximum deposit is 50000 and machine accepts only 100rs notes ')

    def withdraw(self):
        continue_withdraw = True
        while continue_withdraw:
            for i in range(3):
                withdraw = int(input('Enter withdrawal amount: '))
                if self.bal == 500:
                    print('Available balance is 500. You cannot withdraw further.')
                    break
                elif withdraw < self.bal:
                    if 100 <= withdraw <= 20000 and withdraw % 100 == 0:
                        self.bal -= withdraw
                        print('Available balance is:', self.bal)
                    else:
                        print(
                            'Minimum withdraw is 100, maximum withdraw is 20000, and machine accepts only 100rs notes.')
                else:
                    print('You cannot withdraw an amount greater than your balance.')
                user_input = input('Do you want to continue? Type y or n: ')
                if user_input != 'y':
                    continue_withdraw = False
                    break
            if not continue_withdraw:
                break
        print("You've reached the maximum limit or exited the withdrawal process.")

    def balEnquiry(self):
        print('Your current balance is:', self.bal)

    def ViewOptions(self):
        while(True):
            print('1.Deposit\n2.Withdraw\n3.Balance Enquiry\n0.Exit')
            op = int(input('choose your option :'))
            if op==1:
                obj.deposit()
            elif op==2:
                obj.withdraw()
            elif op==3:
                obj.balEnquiry()
            else:
                exit(0)


    def validation(self):
        print('Welcome to ABC Bank')
        for i in range(3):
            userPin = int(input('Enter pin :'))
            if userPin==1234:
                obj.ViewOptions()
                break
            else:
                if i==2:
                    print('card blocked...try again after 1hr')
                    break
                print('Invalid Pin please try again')


obj=Bank()
obj.validation()