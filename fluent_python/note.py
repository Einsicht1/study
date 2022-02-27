class Car:
    pass


class G7(Car):
    pass


class Avante(Car):
    pass



print(Car.__subclasses__())

for car in Car.__subclasses__():
    print(car.__name__)
