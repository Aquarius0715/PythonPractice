class Creature:
    def alive(self):
        print("生きている")

class Human(Creature):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def self_intro(self):
        print("私の名前は{}です。年齢は{}才です。".format(self.name, self.age))

nutmeg_man = Human("nutmeg_man", 23)
nutmeg_man.self_intro()
nutmeg_man.alive()
