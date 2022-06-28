# class person():
#     def __init__(self):
#         self.first_name='Umesh'
#         self.last_name='Kumar'
#         self.age=25
#         print('Hello World')
# p=person()
# print(p.last_name)

class person():
    def __init__(self,fn,ln,age):
        self.first_name=fn
        self.last_name=ln
        self.age=age
        print('Hello World')
p=person('umesh','kumar',25)
print(p.last_name)