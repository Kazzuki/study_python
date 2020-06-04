class Person(object):
    def talk(self):
        print('talk')
    def run(self):
        print('person run')

class Car(object):
    def run(self):
        print('car run')

#Carクラスが優先される
class PersonCarRobot(Car, Person):
    def fly(self):
        print('fry')

person_car_robot = PersonCarRobot()
person_car_robot.talk()
#Carクラスが優先されるので
person_car_robot.run() #car run

person_car_robot.fly()
