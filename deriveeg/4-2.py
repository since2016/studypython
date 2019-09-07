
class Programmer(object):
    def __new__(cls, *args, **kwargs):
        print("call __new__method")
        print(args)
        return super(Programmer, cls).__new__(cls, *args, **kwargs)


    def __init__(self, name, age):
        print("__call__init")
        self.name = name
        self.age=age


if __name__ == '__main__':
    programmer = Programmer('alpha', 80)
    print(programmer.__dict__)