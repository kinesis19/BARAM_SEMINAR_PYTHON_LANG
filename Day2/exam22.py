class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Brand: {self.brand}, Model : {self.model}")
    
car1 = Car("현대", "아이오닉5")
car2 = Car("기아", "K9")

car1.display_info()
car2.display_info()