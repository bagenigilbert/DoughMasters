# Welcome to Pizza Paradise 🍕
Hey there! I'm Gilbert Bagen, and I'm excited to introduce you to Pizza Paradise - a web application that's all about our love for pizza! 🚀

## What's Pizza Paradise?
Pizza Paradise is where pizza dreams come true. It's your go-to place for managing your favorite pizza joints and their delectable pizza offerings. With a user-friendly interface and a robust backend powered by Flask and SQLAlchemy, you'll effortlessly create, update, and explore a world of pizza possibilities. 🌍🍕

## Let's Get Started 🚀
### What You'll Need
Before you dive in, make sure you've got the essentials:

Python 3.x
Flask
Flask-SQLAlchemy
Flask-Migrate
A modern web browser
How to Set Up
Clone this Repository:

git clone https://github.com/yourusername/pizza-paradise.git
Navigate to the Project Directory:


cd pizza-paradise
Create a Virtual Environment (Optional, but a good practice):



python -m venv venv
On macOS and Linux:

source venv/bin/activate
Install Dependencies:


pip install -r requirements.txt
Initialize the Database:


flask db init
Migrate the Database:


flask db migrate
Apply Migrations:

flask db upgrade
Start the Application:

flask run
Now, you should see the magic happening at http://localhost:5003.

## Explore the Features 🍴
Restaurant Management: Easily create, update, and delete restaurant entries.
Pizza Catalog: Maintain a list of mouthwatering pizzas with detailed ingredient information.
Restaurant-Pizza Association: Link restaurants and pizzas, complete with pricing details.
API Access: We've got RESTful API endpoints for programmatic interaction.
Data Serialization: Everything's served up in JSON format for seamless integration.
How to Use
Browse Restaurants: Go to /restaurants to see a list of all registered restaurants.

Explore Pizzas: Check out /pizzas to discover the various pizzas available.

Add a Restaurant: Create a new restaurant by making a POST request to /restaurants with the restaurant's details.

Add a Pizza: Whip up a new pizza entry with a POST request to /pizzas.

Associate Pizza with a Restaurant: Link a pizza with a restaurant by sending a POST request to /restaurant_pizzas.

Delete a Restaurant: Remove a restaurant using a DELETE request to /restaurants/<restaurant_id>.

For in-depth API documentation, dive into the API Endpoints section below.

## API Endpoints 🚀
GET /restaurants: Get a list of all restaurants.
GET /restaurants/{id}: Get the details of a specific restaurant and its associated pizzas.
DELETE /restaurants/{id}: Say goodbye to a restaurant and all its data.
GET /pizzas: Check out the complete list of mouthwatering pizzas in the system.
POST /restaurant_pizzas: Create a delicious relationship between a restaurant and a pizza.
Get Involved 🙌
We'd love your contributions! If you're eager to make Pizza Paradise even more amazing, follow these steps:

## Fork this Repository.
Create a New Branch: git checkout -b feature/your-feature-name.
Commit Your Changes: git commit -m 'Add some feature'.
Push Your Branch: git push origin feature/your-feature-name.
Submit a Pull Request.
## License 📝
This project is licensed under the MIT License. You can find all the details in the LICENSE file.

Thanks for choosing Pizza Paradise. Dive in, explore, and savor the world of pizzas! 🍕 If you have any questions or ideas, don't hesitate to reach out.

Enjoy your pizza journey!

## Author: Gilbert Bagen

