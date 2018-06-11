""" This is an example of a class definition with a display cunction in python"""
class Students:
    def __init__(self, name, age, sex, grade):
        self.name = name 
        self.age = age 
        self.sex = sex
        self.grade = grade

    def displayStudent(self):
        return("The Student " + self.name + " is " + str(self.age) + " years of age,  a " + self.sex + " and he had " + str(self.grade) + " in the final exam")


student1 = Students("Jacob", 17, "male", 45)
student1.displayStudent()


