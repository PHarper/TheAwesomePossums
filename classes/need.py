# items that the user NEEDS

class Need():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.nameList = []
        self.priceList = []
        self.quantityList = []
        self.get_List()



    def get_budgetTotal(self):
        # grab budget total from user input from web app
        #set the given value as a datamember (then return that value in the set method)


        pass

    def set_budgetTotal(self):
        #return self.budgetTotal

        pass

    def get_name(self):
        #from user input from website
        #set name as self.name (return in SET method)
        pass

    def get_price(self):
        #from user input from website
        pass

    def get_quantity(self):
        #from user input on website
        pass

    def set_name(self):
        self.nameList.append(self.name)

    def set_price(self):
        self.priceList.append(self.price)

    def set_quantity(self):
        self.quantityList.append(self.quantity)

    def get_List(self):
        self.itemDict = {}
        self.itemDict.update({self.name:[self.price,self.quantity]})
        return self.itemDict

# get_list returns '<__main__.Need instace at 0x2aab48>'  (for example)



