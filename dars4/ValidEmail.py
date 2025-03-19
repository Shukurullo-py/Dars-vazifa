import re

class ValidEmailDeskriptor:
    def __init__(self,name):
        self.name = name

    def __get__(self,instance,owner):
        return instance.__dict__.get(self.name)

    def __set__(self,instance,value):
        p = r"^[a-zA-Z0-9]+@(gmail|mail)\.(com|uz)$"
        if re.match(p,value):
            instance.__dict__[self.name] = value
        else:
            raise ValueError("false")
            

class ValidEmail:
    res = ValidEmailDeskriptor("res")

p1 = ValidEmail()

p1.res = "Shukurullo000@gmail.com"
print(p1.res)