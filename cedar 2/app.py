from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate
from datetime import datetime
import pytz

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

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
    is_admin = db.Column(db.Boolean, default=False)  # Indicates if the user is an admin

    
    
@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

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
        
        #user = User.query.filter_by(username=username).first()
        user = User.query.filter_by(username='admin').first()  
        if user:
            user.isAdmin = True  
            db.session.commit()

        
        if user and user.password == password:
            if user.isAdmin == True :
                return render_template('admin.html') 
          #  else:
             #  return redirect(url_for('menu')) 
            #else:
               # return(url_for('/menu'))
        else:
            return redirect(url_for('menu')) #SET ANY PAGE HERE. I JUST PUT MENU AS A PLACEHOLDER FOR REGULAR USERS
    
    return render_template('login.html')





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
   

@app.route('/menu')
def menu():
    food_items = FoodItem.query.all()

    #This is a function that will redirect the user if they hit the order tab outside of the time when the store is open (from 11AM to 7PM)
    #if datetime.now(tz_NY) > 06:59:59 and datetime.now(tz_NY) < 23:00:00  
    return render_template('menu.html', food_items=food_items)
    #else
    #return "The store is currently closed and orders are not available to be taken."

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
