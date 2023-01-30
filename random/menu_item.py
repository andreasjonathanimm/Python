class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = str(price)
    def info(self):
        return 'Menu : ' + self.name + '   Harga : $' + self.price