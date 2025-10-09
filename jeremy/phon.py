class Phone():

    def __init__(self, name, storage, battery_life, price):
        self.name = name
        self.storage = storage
        self.battery_life = battery_life
        self.price = price

    def description(self):
        print(f'Name: {self.name}')
        print(f'Storage: {self.storage} GB')
        print(f'Battery life: {self.battery_life} hrs')
        print(f'Price: ${self.price}')

    def discount(self, percent):
        self.price = self.price * percent / 100
        print(f'Discounted {percent}% from {self.name}!')
        print(f'{self.name} is now ${self.price}.')

    def compare(self, other):
        if self.price > other.price:
            cheaper = other.name
        elif self.price < other.price:
            cheaper = self.name
        elif self.price == other.price:
            print('Both phones are the same price!')
            return
        print(f'{cheaper} is cheaper!')

phone1 = Phone('AAAAA', 1, 3, 9999999)
phone1.description()

phone2 = Phone('AaAaA', 1000, 67, 9999999)
phone2.discount(20)
phone1.compare(phone2)