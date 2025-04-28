class User:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

class Order:
    def __init__(self, id, user_id, product_id, quantity):
        self.id = id
        self.user_id = user_id
        self.product_id = product_id
        self.quantity = quantity

class Address:
    def __init__(self, id, user_id, street, city, state, zip_code):
        self.id = id
        self.user_id = user_id
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code