from cargo import Cargo

class Store:

    def __init__(self, location :str, cargos: list[Cargo], max_size_cargo :int = 1000):
        self._location = location
        self._max_size_cargo = max_size_cargo
        try:
            if sum([cargo.get_size() for cargo in cargos]) > self._max_size_cargo:
                raise ValueError('Превышено количество товаров на складе , ошибка!!!')

            self._current_cargo = cargos

        except ValueError as e:
            print(e)

    def check_availability(self,cargos : list[Cargo]):
        try:
            absent_cargos = []
            for cargo in cargos:
                if not cargo in self._current_cargo:
                    absent_cargos.append(cargo.get_name())

            if len(absent_cargos) == 0:
                return True
            else:
                raise ValueError(str(absent_cargos))
        except ValueError as e:
            print(e)



    def check_place(self,cargos : list[Cargo]) -> bool:
        if sum([cargo.get_size() for cargo in cargos]) + sum([cargo.get_size() for cargo in self._current_cargo]) > self._max_size_cargo:
            return False
        else:
            return True

    """def add_cargo(self, cargos :list[Cargo]):
        self._current_cargo += cargos


    def take_cargo(self, cargos :list[Cargo]):
        self._current_cargo = [cargo for cargo in self._current_cargo if cargo not in cargos]"""
