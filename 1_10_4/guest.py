class Client:
    def __init__(self, first_name, second_name, money):
        self.first_name = first_name
        self.second_name = second_name
        self.money = money

    def print_client(self):
        print(f"Клиент {self.first_name} {self.second_name}. Баланс: {self.money} рублей")


class Guest(Client):
    def __init__(self, first_name, second_name, city, status):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.status = status

    def print_guest(self):
        print(f"{self.first_name} {self.second_name}, г. {self.city}, статус {self.status}")


guest_1 = Guest("Иван", "Петров", "Москва", "Наставник")
guest_2 = Guest("Алексей", "Соколов", "Новосибирск", "Волонтер")
guest_3 = Guest("Петр", "Иванов", "Москва", "Волонтер")

guests = [guest_1, guest_2, guest_3]
for guest in guests:
    guest.print_guest()
