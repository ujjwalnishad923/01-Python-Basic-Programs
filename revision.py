class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum+=value
        print("Hii", self.name,"your avg score is:" ,sum/3)
    
s1 = Student("ujjwal Kumar nishad",[89, 85, 99])
s1.get_avg()