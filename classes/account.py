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


class Budget:
    def __init__(self,budgetType, balance):
        self.budgetType = budgetType
        self.balance = balance


    def purchase(self, itemCost):
		self.balance -= itemCost
		
	def getBalance(self):
		return self.balance

class Saving(Budget):
    def __init__(self, balance):
		Budget.__init__(self, accountType)
		newbal()ftallin
		
	def deposit(self, amount):
		self.balance += amount
		


class monthlyBudget(Budget):
    
    def __init__(self, new_bal)
    	Budget.__init__(self,budgetType, balance)
    	self.new_bal = new_bal
    
    def setMonthly(self,amount):
		return self.new_bal
		


