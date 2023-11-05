from typing import Any


class Car :
    def __init__(self) -> None:
        self._type = None

    def get_type(self) :
        return self._type

class SportsCar(Car):
    def __init__(self) -> None:
        self._type = 'Sport Car'

class FamilyCar(Car):
    def __init__(self) -> None:
        self._type = 'Family Car'

class ElectricCar(Car):
    def __init__(self) -> None:
        self._type = 'Electric Car'

class FactoryCar:
    def __init__(self) -> None:
        self._cars = {}
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass

    def register_car(self, car_type, car_class):
        self._cars[car_type] = car_class

    def create_car(self,car_type) :
        if car_type in self._cars :
            return self._cars[car_type]()
        raise ValueError(f'Invalid type car {car_type}')
    
if __name__ == '__main__' :

    factory = FactoryCar()
    factory.register_car("sports", SportsCar)
    factory.register_car("family", FamilyCar)
    factory.register_car("electric", ElectricCar)

    car = factory.create_car('sports')
    print(car.get_type())


