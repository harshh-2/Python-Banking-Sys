class Account:
    def __init__(self,bal,acc,name):
        self.bal=bal
        self.name=name
        self.acc=acc
        print(f"Fetching acc details for {self.name}....")
    def credit(self,amount):
        self.bal += amount
        print("Rs",amount,"credited")
        print("Remaining balance is:",self.bal)
    def debit(self,amount):
        self.bal -= amount
        print("Rs",amount,"debited")
        print("Remaining balance is:",self.bal)
    def bank(self):
        a=input("DEBIT,CREDIT OR CHECK BALANCE:  ").upper()
        if a=='DEBIT':
            b=int(input("Amount to be debited:"))
            if b>self.bal:
                print("Amount exceeds current balance")
            else:
                self.debit(b)
        elif a=="CHECK BALANCE":
            print(f"The current bank balance is : {self.bal}")
        elif a=='CREDIT':
            b=int(input("Amount to be credited:"))
            if b<1:
                print("Amount to be credited should be greater than 1")
            else:
                self.credit(b)
        else:
            print("Invalid operation")
n=int(input("Enter Bank account number:"))
s=0
if n==1234:
    r=input("Enter password:")
    password='123er'
    if r==password:
        s=10000
        name='Karan'
    else:
        print("Incorrect password exitinggg....")
        exit()
elif n==1245:
  r=input("Enter password:")
  password='123qwe'
  if r==password:
        s=75000
        name='rahul'
  else:
        print("Incorrect password exitinggg....")
        exit()
  
elif n==6969:
    r=input("Enter password:")
    password='chimpui'
    if r==password:
        name="Pranay"
        s=12
    else:
        print("Incorrect password exitingg....")
        exit()
   
else:
    print("Account does not exist in this bank")
    exit()
s1=Account(s,n,name)
s1.bank()