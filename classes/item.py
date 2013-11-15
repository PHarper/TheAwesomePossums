#item class  
# will allow a createNew item

#import popularity
import rate


class Item():

        def __init__(self, name, rate, price, popularity):
                self.name = name
                self.rate= rate
                self.price = price
                self.popularity = popularity

        def getName(self):
                return self.name

        def getRank(self):
                return self.rate

        def getPrice(self):
                return self.price

        def getPopularity(self):
                return self.popularity

        def editPrice(self,price):
                self.price = price

        def editRank(self,rank):
                self.rank = rank



        def createNew(self):
                pass


i = Item('book',5,10,10)
i.editPrice(20)
print i.getPrice()
print i

