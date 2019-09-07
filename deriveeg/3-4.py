class Programmer(object):
    def __init__(self, name , age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_hobby(cls):
        return cls.get_hobby

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print(" my name is %s \n I am %s years old" %(self.name, self._age))


class BackendProgrammer(Programmer):
    def __init__(self, name, age, weight, lan):
        super(BackendProgrammer, self).__init__(name, age, weight)
        self.lan = lan

    def self_introduction(self):
        print("my name is %s \n my favorite language is %s \n" %(self.name, self.lan))



def introduce(programer):
    if isinstance(programer, Programmer):
        programer.self_introduction()

if __name__ == '__main__':
    programmer = Programmer('alpha', 26, 80)
    bp = BackendProgrammer('Alpha', 26, 80, 'python')

    introduce(programmer)
    introduce(bp)