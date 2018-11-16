class Dog(object):
    def print_self(self):
        print("大家好,我是xxx,以后请大家多多关照...")

class Xiaotq(Dog):
    def print_self(self):
        print("Hello,everybody,我是你们的大佬,我是xxx...")

def introduce(temp):
    temp.print_self()

dog1 = Dog()
dog2 = Xiaotq()
introduce(dog1)
introduce(dog2)
