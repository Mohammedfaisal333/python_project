import mysql.connector
from mysql.connector import Error
import unittest
class ATM:
    def __init__(self,name,acc_no,balance):
        self.name = "Faisal"
        self.acc_no = acc_no
        self._bank = "SBI"
        self.__pin = 2233
        self.balance = balance
        self.address = 'Karnataka'
    def check_pin(self):
        return self.__pin
    def withdraw(self,amount,pin):
        if self.balance>0 and self.balance>=amount:
            if self.__pin==pin:
                self.balance-=amount
            else:
                print('Incorrect pin')
                self.balance=self.balance
        else:
            print('Insufficient Funds')
            
            return self.balance
    def deposite(self,amount,pin):
            if self.__pin==pin:
                self.balance+=amount
                print('Deposited Sucessfully!')
            else:
                print('Incorrect pin')
            return self.balance
        
    def change_pin(self,newpin):
            self.__pin=newpin
            return(f'pin Change Successfull {self.__pin}')    
    
    def miniStatement(self):
            return f'Name is: {self.name},Bank is: {self.bank},Balance is: {self.balance}'
class ATMAdmin:
    def __init__(self, host, user, password, database):
        try:
            self.conn = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            if self.conn.is_connected():
                print("Connected to MySQL Database")
                self.cursor = self.conn.cursor()
            else:
                print("Connected to MySQL Failed.")
                self.cursor = None
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            self.conn = None
            self.cursor = None
    def add_acc_holder(self,acc_no):
        if self.cursor is None:
            print("Cannot add Account Holder Details. No database Connection.")
            return
        try:
            query = "INSERT INTO account (acc_no, name, bank, balance) VALUES (%s, %s, %s, %s)"
            values = (account.acc_no, account.name, account.bank, account.balance)
            print(f"Attempting to insert: {values}")  #Debugging output
            self.cursor.execute(query, values)
            self.conn.commit()
            print(f"Account record for {account.acc_no} added")
        except Error as e:
            print(f"Failed to insert renewal: {e}")
            
            
class TestATMApplicatonSystem(unittest.TestCase):
    def setUp(self):
        self.system = ATMAdmin("localhost", "root", "your_password", "passport_renewal")
        self.record = ATM('Faisal', 123456789,5000)
        self.system.add_renewal(self.record)
        
if __name__=="__main__":
    unittest.main()
    
 
 
 
 
    
print(obj._ATM__pin)
#print(obj.withdraw(1000,2233))
#print(obj.change_pin(2233))
#print(obj.deposite(4500,2233))
print(obj.miniStatement())            
