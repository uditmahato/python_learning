class dog:
    def __init__(self, leg, color, tail):
        self.leg = leg
        self.color = color
        self.tail = tail
        print('Here is the propeties of the dog')
p=dog(4,'black','short')
print(p.leg)
print(p.color)
print(p.tail)
