import math

from store import Store
from cargo import Cargo
from transport import Transport
import random

fuel_cost = {'АИ-98' :2.82, 'АИ-92' :2.5, 'АИ-95' :2.6, 'ДТ' :2.6}
danger_cargo_index = 0.7
usual_cargo_index = 0.3

transfer_danger_cargo_index = 0.5
transfer_usual_cargo_index = 0.2


def _calculate_distance():
    return random.randint(100,1000)


def _check_place(store : Store, cargos :list[Cargo]) -> bool:
    if store.check_place(cargos):
        return True
    else:
        return False

def calculate_cargo_cost(cargos :list[Cargo], distance :int) -> float:
    cargos_total = 0
    for cargo in cargos:
        if cargo.is_dangerous():
            cargos_total += distance * danger_cargo_index * cargo.get_size()
        else:
            cargos_total += distance * usual_cargo_index * cargo.get_size()

    return cargos_total

def calculate_cargo_transfer_time(cargos :list[Cargo]) -> float:
    total_time = 0

    for cargo in cargos:
        if cargo.is_dangerous():
            total_time += cargo.get_size() * transfer_danger_cargo_index
        else:
            total_time += cargo.get_size() * transfer_usual_cargo_index

    return total_time

def _check_availability(store : Store, cargos :list[Cargo]) -> bool:
    if store.check_availability(cargos):
        return True

def calculate_fuel_cost(transport :Transport, distance :int) -> float:
    fuel_quantity = (distance - transport.get_fuel()) * transport.get_expense() / 100
    refuel_number = math.ceil(fuel_quantity/transport.get_fuel_tank())
    return refuel_number * transport.get_fuel_tank() * fuel_cost[transport.get_fuel_type()]

class ControlSystem:
    def __init__(self, transport : list[Transport], service_price :float):
        self._transport = transport
        self._service_price = service_price

    def transport_cargo(self, departure : Store, destination :Store, cargos :list[Cargo]) ->tuple[float,float]:
        if _check_place(destination,cargos) and _check_availability(departure,cargos):
            distance = _calculate_distance()
            transport = self._get_transport(cargos)

            total_cost = calculate_fuel_cost(transport, distance) + calculate_cargo_cost(cargos, distance)
            total_time = distance / 70 * 60 + calculate_cargo_transfer_time(cargos) * 2  # 70 - средняя скорость езды по беларуси

            return total_time, total_cost

        else:
            return 0,0

    def _get_transport(self,cargos :list[Cargo]):
        return random.choice([transport for transport in self._transport if transport.get_max_cargo_size() <= sum([cargo.get_size() for cargo in cargos])])

