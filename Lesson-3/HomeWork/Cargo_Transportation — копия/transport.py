from trailer import Trailer

class Transport:
    def __init__(self, fuel_tank :int, fuel :int, expense :int, fuel_type :str = 'Petrol'):
        self._fuel_tank = fuel_tank
        self._fuel = fuel
        self._expense = expense
        self._fuel_type = fuel_type


    def get_fuel_tank(self):
        return self._fuel_tank

    def get_fuel(self):
        return self._fuel

    def get_expense(self):
        return self._expense

    def get_fuel_type(self):
        return self._fuel_type

    def get_max_cargo_size(self):
        pass


class Truck(Transport):
    def __init__(self, fuel_tank :int, fuel :int, expense :int, max_cargo_size :int,fuel_type :str):
        super().__init__(fuel_tank, fuel, expense, fuel_type)
        self._max_cargo_size = max_cargo_size

    def get_max_cargo_size(self):
        return self._max_cargo_size

class Wagon(Transport):
    def __init__(self, fuel_tank :int, fuel :int, expense :int, fuel_type :str = 'Petrol'):
        super().__init__(fuel_tank, fuel, expense, fuel_type)
        self._trailer = None

    def add_trailer(self, trailer :Trailer):
        self._trailer = trailer

    def get_max_cargo_size(self):
        if self._trailer:
            return self._trailer.get_max_cargo_size()


