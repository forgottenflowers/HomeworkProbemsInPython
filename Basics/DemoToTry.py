class Person:
    """ A person class """

    def __init__(self, name, age, gender):

        print("__init__ Person")
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        """ Say hello """
        print("Hello. My name is {}".format(self.name))

    def has_birthday(self):
        self.age += 1


class Teacher(Person):
    """ A teacher class """

    def __init__(self, name, age, gender):
        print("__init__ Teacher")
        Person.__init__(self, name, age, gender)

    def gives_grade(self):
        print("You get a 1.7")


class Student(Person):
    """ A student class """

    def __init__(self, name, age, gender):
        print("__init__ Student")
        Person.__init__(self, name, age, gender)

    def receives_grade(self):
        print("I get a 1.7")


class Teacher(Person):
    """ A teacher class. """

    def __init__(self, name, age, gender):
        print("__init__ a Teacher class ")
        Person.__init__(self, name, age, gender)

    def gives_grade(self):
        print("Your grade is: ", 1.3)
