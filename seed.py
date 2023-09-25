from app import db, app
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    # Create Restaurants
    restaurant1 = Restaurant(name="Dominion Pizza", address="Good Italian, Ngong Road, 5th Avenue")
    restaurant2 = Restaurant(name="Pizza Hut", address="Westgate Mall, Mwanzi Road, Nrb 100")

    # Create Pizzas
    pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
    pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")

    # Add Restaurants and Pizzas to the database
    db.session.add(restaurant1)
    db.session.add(restaurant2)
    db.session.add(pizza1)
    db.session.add(pizza2)
    db.session.commit()

    # Create RestaurantPizzas
    restaurant_pizza1 = RestaurantPizza(price=10.99, pizza_id=pizza1.id, restaurant_id=restaurant1.id)
    restaurant_pizza2 = RestaurantPizza(price=12.99, pizza_id=pizza2.id, restaurant_id=restaurant1.id)
    restaurant_pizza3 = RestaurantPizza(price=11.99, pizza_id=pizza1.id, restaurant_id=restaurant2.id)

    # Add RestaurantPizzas to the database
    db.session.add(restaurant_pizza1)
    db.session.add(restaurant_pizza2)
    db.session.add(restaurant_pizza3)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_data()
