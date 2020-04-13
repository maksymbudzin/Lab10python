class Gem:
    price_in_dollars_for_100g = 120000

    def __init__(self, name=None, price=None, country=None,
                 wight=None,
                 number_of_carats=None, year_of_opening=None):
        self.name = name
        self.price = price
        self.country = country
        self.weight = wight
        self.number_of_carats = number_of_carats
        self.year_of_opening = year_of_opening

    @staticmethod
    def staticmethod():
        return Gem.price_in_dollars_for_100g

    def __str__(self):
        name = "Name: {0}\n".format(self.name)
        price = "price: {0}\n".format(self.price)
        country = "Country: {0}\n".format(self.country)
        weight = "weight : {0}\n".format(
            self.weight)
        number_of_carats = "Number of carats: {0}\n".format(self.number_of_carats)
        year_of_opening = "Year of opening: {0}\n".format(self.year_of_opening)
        price_in_dollars_for_100g = "Price in millions of dollars: {0}\n".format(
            Gem.price_in_dollars_for_100g)
        return name + price + country + weight + number_of_carats + \
               year_of_opening + price_in_dollars_for_100g

    def __del__(self):
        print("Delete " + self.__class__.__name__ + " | Object ID: " + str(id(self)))
        return

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_country(self):
        return self.country

    def set_country(self, country):
        self.country = country

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def weight(self):
        return self.weight

    def weight(self, weight):
        self.weight = weight

    def get_number_of_carats(self):
        return self.number_of_carats

    def set_number_of_carats(self, number_of_carats):
        self.number_of_carats = number_of_carats

    def get_year_of_opening(self):
        return self.year_of_opening

    def set_year_of_opening(self, year_of_opening):
        self.year_of_opening = year_of_opening

