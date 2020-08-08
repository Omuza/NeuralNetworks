from classtools import AttrDisplay

class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    
    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)

    def giveRaise(self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)

class Department:
    def __init__(self, *args):
        self.members = list(args)

    def addMembers(self, person):
        self.members.append(person)

    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    
    def showAll(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Ball')
    ann = Person('Ann Ball', job ='Data Scientist', pay = 50000)
    janet = Manager('Janet Jackson', pay = 70000)

    print(ann)
    #ann.giveRaise(0.07)
    #print(ann)
    #janet.giveRaise(0.09)
    #print(janet)

    development = Department(bob, ann)
    development.addMembers(janet)
    development.giveRaises(.15)

    development.showAll()

    #print(list(bob.__dict__.keys()))
    


    

    

