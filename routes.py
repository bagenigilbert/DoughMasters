# Import necessary modules
from flask import jsonify, request, abort,render_template

# Import the Flask application and database instance
from app import app, db

# Import the models for Restaurant, Pizza, and RestaurantPizza
from models import Restaurant, Pizza, RestaurantPizza
@app.route('/', methods=['GET'])
def home():
     return render_template('home.html')

# Define a route to retrieve all restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    # Query all restaurants from the database
    restaurants = Restaurant.query.all()
    
    # Serialize the restaurant data to JSON and return it
    return jsonify([restaurant.serialize() for restaurant in restaurants])

# Define a route to retrieve a specific restaurant by ID
@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    # Query the restaurant by its ID
    restaurant = Restaurant.query.get(id)
    
    if restaurant:
        # Serialize the restaurant data with associated pizzas to JSON and return it
        return jsonify(restaurant.serialize_with_pizzas())
    else:
        # Return an error message with a 404 status if the restaurant is not found
        return jsonify({'error': 'Restaurant not found'}), 404

# Define a route to delete a restaurant by ID
@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    # Query the restaurant by its ID
    restaurant = Restaurant.query.get(id)
    
    if restaurant:
        # Delete all RestaurantPizza entries associated with this restaurant
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        
        # Delete the restaurant and commit the changes to the database
        db.session.delete(restaurant)
        db.session.commit()
        
        # Return a 204 (No Content) status to indicate successful deletion
        return '', 204
    else:
        # Return an error message with a 404 status if the restaurant is not found
        return jsonify({'error': 'Restaurant not found'}), 404

# Define a route to retrieve all pizzas
@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    # Query all pizzas from the database
    pizzas = Pizza.query.all()
    
    # Serialize the pizza data to JSON and return it
    return jsonify([pizza.serialize() for pizza in pizzas])

# Define a route to create a new restaurant-pizza association
@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    # Get the JSON data from the request
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Check if the required data is provided
    if not (price and pizza_id and restaurant_id):
        # Return a JSON response with validation errors and a 400 status code
        return jsonify({'errors': ['validation errors']}), 400

    # Create a new RestaurantPizza entry, add it to the database, and commit
    restaurant_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(restaurant_pizza)
    db.session.commit()

    # Retrieve and return the serialized pizza data
    return jsonify(Pizza.query.get(pizza_id).serialize())
