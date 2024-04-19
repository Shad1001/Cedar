from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
<<<<<<< HEAD
=======
from flask_migrate import Migrate
import datetime
>>>>>>> Gian

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
<<<<<<< HEAD

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(255))  

class User(db.Model):
	user_id = db.Column(db.Integer, primary_key=True)
	fullname = db.Column(db.String(100), nullable=False)
	username = db.Column(db.String(50), unique=True, nullable=False)
	password = db.Column(db.String(250), nullable=False)
    
    
@app.route('/')
def index():
    return render_template('homepage.html')

=======
migrate = Migrate(app, db)

##################################################
#   User Class
##################################################
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)

##################################################
#   Food Class
##################################################
class Food(db.Model):
    foodID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)

##################################################
#   Order Class
##################################################
class Order(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)
    userID = db.Column(db.Float, nullable=False)

##################################################
#   Order_Detail Class
##################################################
class Order_Detail(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    foodID = db.Column(db.DateTime, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    extendedPrice = db.Column(db.Float, nullable=False)

##################################################
#   app.route for /
##################################################
@app.route('/')
def index():
    return render_template('home.html')

##################################################
#   app.route for /admin
##################################################
>>>>>>> Gian
@app.route('/admin')
def admin():
    return render_template('admin.html')

<<<<<<< HEAD
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
    
    fullname = request.form['fullname']
    username = request.form['username']
    password = request.form['password']

    
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        
        return "Username already taken. Please choose another username."

    
    new_user = User(fullname=fullname, username=username, password=password)

    
    db.session.add(new_user)
    db.session.commit()

    
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            
            return redirect(url_for('admin'))
        else:
            
            return "Invalid username or password."
    
    return render_template('login.html')




=======
##################################################
#   app.route for /add-food-item
##################################################
>>>>>>> Gian
@app.route('/add-food-item', methods=['POST'])
def add_food_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
<<<<<<< HEAD
        image_url = request.form.get('image_url', '') 
        
        new_item = FoodItem(name=name, price=float(price), category=category, image_url=image_url)
=======
        
        new_item = Food(name=name, price=float(price), category=category)
>>>>>>> Gian
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('admin'))
    
<<<<<<< HEAD
    return redirect(url_for('admin'))  



@app.route('/delete-food-item', methods=['POST'])
def delete_food_item():
    item_id = request.form['item_id']
=======
    return redirect(url_for('admin'))

##################################################
#   app.route for /delete-food-item
##################################################
@app.route('/delete-food-item', methods=['POST'])
def delete_food_item():
>>>>>>> Gian
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']

<<<<<<< HEAD
   
    item = FoodItem.query.filter_by(id=item_id, name=name, price=price, category=category).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('admin'))  
   

@app.route('/menu')
def menu():
    food_items = FoodItem.query.all()
    return render_template('menu.html', food_items=food_items)

=======
    item = Food.query.filter_by(name=name, price=float(price), category=category).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('admin'))    

##################################################
#   app.route for /register
##################################################
@app.route('/register', methods=['GET'])
def signup_form():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return "Username already taken. Please choose another username."

    new_user = User(username=username, password=password)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('login'))

##################################################
#   app.route for /login
##################################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username='admin').first()  
        if user:
            user.isAdmin == True
            db.session.commit()

        if user and user.password == password:
            if user.isAdmin == True :
                return render_template('admin.html') 
        else:
            return redirect(url_for('menu')) #SET ANY PAGE HERE. I JUST PUT MENU AS A PLACEHOLDER FOR REGULAR USERS
    
    return render_template('login.html')

##################################################
#   app.route for /menu
##################################################
@app.route('/menu')
def menu():
    breakfast = Food.query.filter(Food.category == "Breakfast")
    appetizers = Food.query.filter(Food.category == "Appetizers")
    coldSandwiches = Food.query.filter(Food.category == "Cold Sandwiches")

    return render_template('menu.html', breakfast=breakfast, appetizers=appetizers, coldSandwiches=coldSandwiches)

##################################################
#   app.route for /add-order-item
##################################################
@app.route('/add-order-item', methods=['GET', 'POST'])
def add_order_item():
    if request.method == 'POST':
        date = datetime.datetime.now()
        subTotal = 0
        tax = 0.06625
        total = 0
        userID = 1

        new_Order = Order(date=datetime, subTotal=float(subTotal),
                         tax=float(tax), total=float(total), userID=userID)
        db.session.add(new_Order)

        finish == False
        while finish != True:
            new_Order_Detail = Order_Detail(orderID=orderID, foodID=foodID, quantity=quantity,
                                            price=float(price), extendedPrice=float(extendedPrice))
            db.session.add(new_Order_Detail)

            if finish == True: #request.method == finish button
                break

            db.session.commit()

        return redirect(url_for('order'))

    else:
        return 'Cart is empty'

##################################################
#   main function
##################################################
>>>>>>> Gian
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
