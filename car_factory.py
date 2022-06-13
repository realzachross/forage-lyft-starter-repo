from servicables.capulet_engine import CapuletEngine
from servicables.sternman_engine import SternmanEngine
from servicables.willoughby_engine import WilloughbyEngine
from servicables.nubbin_battery import Nubbin
from servicables.spindler_battery import Spindler
from car import Car
from datetime import date


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date,
                        current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)

    @staticmethod
    def create_palindrome(
            current_date: date, last_service_date: date, warning_light_on: bool):
        engine = SternmanEngine(warning_light_on)
        battery = Spindler(current_date, last_service_date)
        car = Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date,
                         current_mileage: int, last_service_mileage: int):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        car = Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date,
                      current_mileage: int, last_service_mileage: int):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = Nubbin(last_service_date, current_date)
        car = Car(engine, battery)
