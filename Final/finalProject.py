class Cook:
    def __init__(self,name):
        self.name=name
        
    def cooking(self):
        print("The "+self.name+" is cooking!")
        print("Bon appetit already!")
         
        
class Soup(Cook):
    def __init__(self, name, water,oil,salt,tomatoPaste):
        super().__init__(name)
        self.water=water
        self.oil=oil
        self.salt=salt
        self.tomatoPaste=tomatoPaste
        
    def recipe(self):
        print("First we put "+self.oil+" of oil in the pot and turn on the bottom.")
        print("Then we add "+self.tomatoPaste+" of our tomato paste and "+self.salt+" of salt and cook a little.")
        print("After we add "+self.water+" of water.We close lid of the pot.")

        

class Meat(Cook):
    def __init__(self, name,meatc ,oil,salt):
        super().__init__(name)
        self.meatc=meatc
        self.oil=oil
        self.salt=salt
        
    def recipe(self):
        print("First we put "+self.oil+" of oil in the pot and turn on the bottom.")
        print("Then we add "+self.meatc+" of meat and "+self.salt+" of salt and cook a little.")
        print("After we close lid of the pot.")
        
        
class Cake(Cook):
    def __init__(self, name,milk, egg,sugar,oil,fame,bakingPowder):
        super().__init__(name)
        self.milk=milk
        self.egg=egg
        self.sugar=sugar
        self.oil=oil
        self.fame=fame
        self.bakingPowder=bakingPowder
        
        
    def recipe(self):
        print("First we put "+self.egg+" of egg and "+self.sugar+" of sugar the pot and we whisk until the foam is foam.")
        print("Then we add "+self.milk+" of milk and "+self.oil+" of oil and we mix until well mixed.")
        print("And then we add "+self.bakingPowder+" of bakingPowder and "+self.fame+" of fame and we mix until well mixed.")
        print("After we put the mixture in the cake mold.We put it in a preheated 180 degree oven and wait 45 minutes.")



choose=input("Welcome! Please choose a recipe.Soup -> 1, Meat -> 2, Cake -> 3. Selection: ")

if (choose=="1"):
    cookName=input("Give soup's name: ")
    waters=input("Enter the amount of water: ")
    oils=input("Enter the amount of oil: ")
    salts=input("Enter the amount of salt: ")
    tomatoPastes=input("Enter the amount of tomato paste: ")
    print()
    
    cooks=Soup(cookName,waters,oils,salts,tomatoPastes)
    cooks.recipe()
    cooks.cooking()
        
elif (choose=="2"):
    cookName=input("Give soup's name: ")
    meats=input("Enter the amount of meat: ")
    oils=input("Enter the amount of oil: ")
    salts=input("Enter the amount of salt: ")
    print()
    
    cooks=Meat(cookName,meats,oils,salts)
    cooks.recipe()
    cooks.cooking() 
    
elif (choose=="3"):
    cookName=input("Give soup's name: ")
    milks=input("Enter the amount of milk: ")
    eggs=input("Enter the amount of eggs: ")
    sugars=input("Enter the amount of sugars: ")
    oils=input("Enter the amount of oil: ")
    fames=input("Enter the amount of fames: ")
    bakingPowders=input("Enter the amount of bakingPowders: ")
    print()
    
    cooks=Cake(cookName,milks,eggs,sugars,oils,fames,bakingPowders)
    cooks.recipe()
    cooks.cooking() 
    
else:
    print("Please check your selection!")














        