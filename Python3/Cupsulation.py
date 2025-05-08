class Creature:
    def alive(self):
        print("生きている")

class Human(Creature):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def self_intro(self):
        print("私の名前は{}です。年齢は{}才です。".format(self.name, self.__age))

    def getAge(self):
        return self.__age

    def setAge(self, newAge):
        self.__age = newAge
        
nutmeg_man = Human("nutmeg_man", 23)
nutmeg_man.setAge(22)
nutmeg_man.self_intro()
nutmeg_man.alive()
