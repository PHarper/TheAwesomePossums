#Account class (for Checking and Savings)

#stores Username, Email, Password from user

class User:
    def __init__(self, username, email, password):

        self.username = username
        self.email = email
        self.password = password
        pass

    def get_email(self):
        return self.email
    def get_username(self):
        return self.username
    def get_password(self):
        return self.password

    def __str__(self):
        return 'Username: %s Email: %s Password: %s' %(self.username, self.email, self.password)

class Account:
    def __init__(self, user, accountNumber, balance):
        self.accountNumber = accountNumber
        self.user = user
        self.balance = balance
        #print "Account __init__ = %s" %(self.balance)

    def __str__(self):
        #print "Account __str__ = %s" %(self.balance)
        return 'Username: %s Email: %s Password: %s. Your account number %s has $%.02f remaining' %(self.User.get_username(), self.User.get_email(), self.User.get_password(), self.accountNumber, self.balance)


    def withdraw(self, withdrawAmount):
        newBalance = self.balance - withdrawAmount
        #print "Account withdraw before = %s" %(self.balance)
        if newBalance >= 0:
            self.balance = newBalance
            #print "Account withdraw after = %s" %(self.balance)
        else:
            return "insufficient funds!"

    def deposit(self, depositAmount):
        #print "Account deposit before = %s" %(self.balance)
        if depositAmount > 0:
            newBalance = depositAmount + self.balance
            self.balance = newBalance
            #print "Account deposit after = %s" %(self.balance)
        else:
            return "incorrect amount"

class Saving(Account):
    def __init__(self, User, accountNumber, balance, rate):

        Account.__init__(self, User, accountNumber, balance)
        self.rate = rate
        self.User = User
        self.accountNumber = accountNumber
        self.balance = balance

        #print 'Savings Balance %s' %(self.balance)

    def add_interest(self):
        x= self.rate / 100 / 12 * self.balance
        self.balance += x



class Checking(Account):
    def __init__(self, User, accountNumber, balance, overdraft):
        self.overdraft = overdraft
        Account.__init__(self, User, accountNumber, balance)
        self.User = User
        self.accountNumber = accountNumber
        self.balance = balance
        #print 'Cheching Balance %s' %(self.balance)

    def withdraw(self, withdrawAmount):
        #print self.balance
        newBalance = self.balance - withdrawAmount
        #print 'new Checking balance after withdraw of %s = %s' %(withdrawAmount,newBalance)
        if newBalance > (0 - self.overdraft):
            self.balance = newBalance

            #print 'checking after %s withdraw from %s' %(withdrawAmount, self.balance)
        else:
            return "insufficient funds!"


