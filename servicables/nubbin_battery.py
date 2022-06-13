from battery import Battery


class Nubbin(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        years = self.current_date.year - self.last_service_date.year
        if self.current_date.month < self.last_service_date.month or (self.current_date.month == self.last_service_date.month and self.current_date.day < self.last_service_date.day):
            years -= 1
        return years >= 2
