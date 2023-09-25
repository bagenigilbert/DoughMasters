from app import db

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100))
    pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }

    def serialize_with_pizzas(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': [pizza.serialize() for pizza in self.pizzas]
        }

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(100))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'pizza_id': self.pizza_id
        }
