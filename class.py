class Cars :
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.bre = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car Started")
car1 = Cars()
car1.start()        
            