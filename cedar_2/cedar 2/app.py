
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gianmydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

##################################################
#   User Class: DONE
##################################################
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    isAdmin = db.Column(db.Boolean, default=False)

##################################################
#   Food Class: DONE
##################################################
class Food(db.Model):
    foodID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)

##################################################
#   Order Class: DONE
##################################################
class Order(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    subTotal = db.Column(db.Float, nullable=False, default=0.0)
    tax = db.Column(db.Float, nullable=False, default=0.0625)
    total = db.Column(db.Float, nullable=False, default=subTotal+(subTotal*tax))
    userID = db.Column(db.Float, nullable=False)

##################################################
#   Order_Detail Class: DONE
##################################################
class Order_Detail(db.Model):
    orderID = db.Column(db.Integer, primary_key=True)
    foodID = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    price = db.Column(db.Float, nullable=False)
    extendedPrice = db.Column(db.Float, nullable=False)

##################################################
#   app.route for /: DONE
##################################################
@app.route('/')
def index():
    return render_template('homepage.html')

##################################################
#   app.route for /admin: DONE
##################################################
@app.route('/admin')
def admin():
    return render_template('admin.html')

##################################################
#   app.route for /signup: DONE
##################################################
@app.route('/signup', methods=['GET'])
def signup_form():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():
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
#   app.route for /login: DONE
##################################################
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        #user = User.query.filter_by(username=username).first()
        user = User.query.filter_by(username='admin').first()  
        if user:
            user.isAdmin = True  
            db.session.commit()

        if user and user.password == password:
            if user.isAdmin == True :
                return render_template('admin.html') 
         
        else:
            return redirect(url_for('menu')) #SET ANY PAGE HERE. I JUST PUT MENU AS A PLACEHOLDER FOR REGULAR USERS
    
    return render_template('login.html')

##################################################
#   app.route for /add-food-item: DONE
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
#   app.route for /delete-food-item: DONE
##################################################
@app.route('/delete-food-item', methods=['POST'])
def delete_food_item():
    name = request.form['name']
    price = request.form['price']
    category = request.form['category']

    item = Food.query.filter_by(name=name, price=price, category=category).first()
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('admin'))  

##################################################
#   app.route for /menu: DONE
##################################################
@app.route('/menu')
def menu():
    food_items = Food.query.order_by(Food.category).all()
    return render_template('menu.html', food_items=food_items)

##################################################
#   app.route for /specials: DONE
##################################################
@app.route('/specials')
def show_specials():
    foodSpecials = Food.query.distinct(Food.category).filter(Food.category == "Specials").all()
    return render_template('specials.html', foodSpecials=foodSpecials)

##################################################
#   app.route for /order: DONE
##################################################
@app.route('/order')
def order():
    food_items = Food.query.order_by(Food.category).all()
    return render_template('order.html', food_items=food_items)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)