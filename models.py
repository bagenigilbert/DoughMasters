# Import the necessary modules (assuming 'db' is imported from 'app')
from app import db

# Define the Restaurant model
class Restaurant(db.Model):
    # Define the columns for the Restaurant table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for a restaurant
    name = db.Column(db.String(50), unique=True, nullable=False)  # Name of the restaurant (unique, cannot be empty)
    address = db.Column(db.String(100))  # Address of the restaurant
    pizzas = db.relationship('RestaurantPizza', backref='restaurant', lazy=True)  # Relationship with RestaurantPizza

    # Serialize method to convert Restaurant data to JSON format
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address
        }

    # Serialize method to include associated pizzas when converting to JSON
    def serialize_with_pizzas(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'pizzas': [pizza.serialize() for pizza in self.pizzas]
        }

# Define the Pizza model
class Pizza(db.Model):
    # Define the columns for the Pizza table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for a pizza
    name = db.Column(db.String(50), nullable=False)  # Name of the pizza (cannot be empty)
    ingredients = db.Column(db.String(100))  # List of ingredients for the pizza

    # Serialize method to convert Pizza data to JSON format
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ingredients': self.ingredients
        }

# Define the RestaurantPizza model
class RestaurantPizza(db.Model):
    # Define the columns for the RestaurantPizza table
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for a restaurant-pizza association
    price = db.Column(db.Float, nullable=False)  # Price of the pizza at the restaurant
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)  # Foreign key to link to a restaurant
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)  # Foreign key to link to a pizza

    # Serialize method to convert RestaurantPizza data to JSON format
    def serialize(self):
        return {
            'id': self.id,
            'price': self.price,
            'restaurant_id': self.restaurant_id,
            'pizza_id': self.pizza_id
        }
