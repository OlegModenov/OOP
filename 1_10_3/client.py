class Client:
    def __init__(self, first_name, second_name, money):
        self.first_name = first_name
        self.second_name = second_name
        self.money = money

    def print_client(self):
        print(f"Клиент {self.first_name} {self.second_name}. Баланс: {self.money} рублей")


client_1 = Client("Иван", "Петров", 50)
client_1.print_client()