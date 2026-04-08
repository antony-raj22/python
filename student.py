class Student:
    def __init__(self, name, marks):
        self.name = name          # public
        self.__marks = marks      # private (encapsulation)

    # add marks
    def add_marks(self, value):
        self.__marks += value
        print("Marks added:", value)

    # abstraction (getter method)
    def get_marks(self):
        return self.__marks

    # display details
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.__marks)