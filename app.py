from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
import datetime

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
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
@app.route('/admin')
def admin():
    return render_template('admin.html')

##################################################
#   app.route for /add-food-item
##################################################
@app.route('/add-food-item', methods=['POST'])
def add_food_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        category = request.form['category']
        
        new_item = Food(name=name, price=float(price), category=category)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('admin'))
    
    return redirect(url_for('admin'))

##################################################
#   app.route for /delete-food-item
##################################################
@app.route('/delete-food-item', methods=['POST'])
def delete_food_item():
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']

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
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
