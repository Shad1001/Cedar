from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

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
    image = db.Column(db.BLOB)

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
        image_url = request.form.get('image_url', '') 
        
        new_item = FoodItem(name=name, price=float(price), category=category, image_url=image_url)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('admin'))
    
    return redirect(url_for('admin'))

##################################################
#   app.route for /delete-food-item
##################################################
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
            user.isAdmin = True  
            db.session.commit()

        if user and user.password == password:
            if user.isAdmin == True :
                return render_template('admin.html') 
        else:
            return redirect(url_for('menu')) #SET ANY PAGE HERE. I JUST PUT MENU AS A PLACEHOLDER FOR REGULAR USERS
    
    return render_template('login.html')

##################################################
#   app.route for /order
##################################################
@app.route('/order')
def menu():
    foodData = Food.query.all()
    return render_template('order.html', foodData=foodData)

##################################################
#   app.route for /add-order-item
##################################################
@app.route('/add-order-item', methods=['GET', 'POST'])
def add_cart_item():
    if request.method == 'POST':
        
        cursor.execute('INSERT')

        #FoodItem.query.
        cartID = FoodItem.id
        price = FoodItem.price

        new_item = Cart(cartID=cartID, price=float(price))

        db.session.add(new_item)
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
