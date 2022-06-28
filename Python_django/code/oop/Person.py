class Person:
    #static variable
    school = "Code Institute"
    principal = "Sr. Principal"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)
    @classmethod
    def print_school(cls):
        print(cls.school)

    @staticmethod
    def print_principal():
        print(Person.principal)


# Person1 = Person("John", 36)
# Person1.myfunc()
# print(Person.school)
# print(Person.principal)
# Person2 = Person("Jane", 27)
# Person2.myfunc()
# print(Person.school)
# print(Person.principal)

p=Person('John',36)
p.print_school()