#dictionary Creation for Class, Subclass, dict
# rate & price(within each SubCategory) > Item(within each SubCategory) > SubCatagoryList(within each Category) > CategoryList
from item import Item


class DefaultDict():
        def __init__(self):
                self.data = open('catlist','r')
                self.basicCategory()
        def basicCategory(self):
                self.MainDict = {}
                for line in self.data.readlines():
                        cindex = line.index(':')
                        main = line[:cindex]
                        count = cindex
                        count += line[cindex:].index(',')
                        sub = line[cindex+1:count]
                        subs = {sub:[]}
                        done = False
                        while done == False:
                                try:
                                        cindex = count + 1
                                        count += line[cindex:].index(',') + 1
                                        subs[line[cindex:count + 1]] = []
                                except ValueError:
                                        done = True
                                self.MainDict[main] = subs
                print self.MainDict
                                
                        
                                
        def subCategory(self, mainCategoryName, subCategoryDict):
                        cat = self.defultDictionary.get(mainCategoryName)
                        if cat==None:
                                pass
                        if subCategoryDict in self.defultDictionary.get(mainCategoryName):
                                pass
                        self.defaultDictionary[mainCategoryName].append(subCategoryDict)

                        
        
        
        def itemCreate(self,name,rate,price,cat,subcat, popularity):
            i = Item(name,rate,price,popularity)
            self.MainDict[cat][subcat].append(i)




                
                
        def rateItem(self, item):
                pass
                
                
        def itemPrice(self, item):
                pass
                
        
a = DefaultDict()
a.itemCreate('toothpaste', 3, 1, 'Pets', 'Pet Grooming,', 0)
a.itemCreate('comb', 78, 40000, 'Pets', 'Pet Grooming,', 10)

print a.MainDict



