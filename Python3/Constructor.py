class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    
    
    def self_intro(self):
        print("私の名前は{}です。年齢は{}歳です。".format(self.name, self.age))


nutmeg_man = Human("nutmeg_man", 23)
ryusei = Human("ryusei", 24)
nutmeg_man.self_intro()
ryusei.self_intro()

