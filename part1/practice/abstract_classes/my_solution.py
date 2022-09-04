from abc import abstractmethod, ABC


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    def start_engine(self):
        print('Двигатель катера запущен')

    def stop_engine(self):
        print('Двигатель катера выключен')

    def move(self):
        print('Катер набирает скорость')

    def stop(self):
        print('Катер остановился')


class Car(Transport):
    def start_engine(self):
        print('Двигатель машины запущен')

    def stop_engine(self):
        print('Двигатель машины выключен')

    def move(self):
        print('Машина набирает скорость')

    def stop(self):
        print('Машина остановилась')


class Electroscooter(Transport):
    def start_engine(self):
        print('Двигатель скутера запущен')

    def stop_engine(self):
        print('Двигатель скутера выключен')

    def move(self):
        print('Скутер набирает скорость')

    def stop(self):
        print('Скутер остановился')


class Person:
    def use_transport(self, tranport: Transport):
        tranport.start_engine()
        tranport.move()
        tranport.stop()
        tranport.start_engine()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
