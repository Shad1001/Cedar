from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

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
        
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            
            return redirect(url_for('admin'))
        else:
            
            return "Invalid username or password."
    
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
    return render_template('menu.html', food_items=food_items)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
