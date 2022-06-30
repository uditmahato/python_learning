class Sunway_Student:
    __school_name='Sunway'
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @classmethod
    def get_school_name(cls):
        return cls.__school_name
    @classmethod
    def set_school_name(cls,name):
        cls.__school_name=name
    @staticmethod
    def get_school_address():
        return 'No.1, Sunway Road, Sunway City'
    def get_student_details(self):
        return 'Name: '+self.name+' Age: '+str(self.age)

    def get_age(self):
        return self.__age
    def set_age(self,new_age):
        if new_age>0:
            self.__age=new_age
        else:
            print('Invalid age')

    
s=Sunway_Student('Umesh',25)
#private variable   
# s.__age()
s.set_age(20)
print(s.get_age())
