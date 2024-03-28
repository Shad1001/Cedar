# Importing the Flask framework as well as the SQLAlchemy for the database connection and CORS (Cross Origin Resource Sharing) which allows cross-origin AJAX makes the website possible to run
from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

#This section initializes our database in SQLLite and it connects SQLLite to our frontend via SQLAlchemy
app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

#This is the Food Item table in our database. It is used for the menu items that the customer adds to their cart and that the admin can modify.
class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))  

#This initializes the User table in our database. It is used for keeping track of which user is logged into the session.
class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(100), nullable=False)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)
    
# This function routes the user to the homepage.     
@app.route('/')
def index():
    return render_template('homepage.html')

# This function routes the user to the admin page.  
@app.route('/admin')
def admin():
    return render_template('admin.html')

# This function routes the user to the signup page page.  
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

#This function actually allows the user to sign up for the website. Via the POST function, it puts the account into the USER table in our database.
@app.route('/signup', methods=['POST'])
def signup():
    
    #These are the required inputs for creating an account, which matches up with the non-primary key attributes of the USER table. 
    fullname = request.form['fullname']
    username = request.form['username']
    password = request.form['password']

    #If there is a user with the username already contained in the database, it will not let a new user make an account with that username.
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        
        return "Username already taken. Please choose another username."

    #If the user fills out the signup form correctly, their information will be added to the database in the USER table. 
    new_user = User(fullname=fullname, username=username, password=password)

    #This adds a new user to the database session.
    db.session.add(new_user)
    db.session.commit()

    #When the user finishes the signup process, they are redirected to the log in page. 
    return redirect(url_for('login'))

# This function allows the user to log into their account, if the account exists in the database. 
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        #When the user logs in to their account, the database is indexed through to find a matching username.
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            
            return redirect(url_for('admin'))
        #If the username or the password is incorrect, it will show the user a message that one of them is incorrect.
        else:
            
            return "Invalid username or password."
    
    return render_template('login.html')


#This function allows the admin to add a food item to the database through the front end using the POST function.
@app.route('/add-food-item', methods=['POST'])
def add_food_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        image_url = request.form.get('image_url', '') 
        
        new_item = FoodItem(name=name, price=float(price), category=category, image_url=image_url)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('admin'))
    
    return redirect(url_for('admin'))  


#This function allows the admin to delete a food item to the database through the front end using the POST function.
@app.route('/delete-food-item', methods=['POST'])
def delete_food_item():
    item_id = request.form['item_id']
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']

   
    item = FoodItem.query.filter_by(id=item_id, name=name, price=price, category=category).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('admin'))  
   
#This function displays the food items on the menu. 
@app.route('/menu')
def menu():
    food_items = FoodItem.query.all()
    return render_template('menu.html', food_items=food_items)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
