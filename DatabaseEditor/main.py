from flask import Flask, render_template, request, jsonify, redirect, url_for
from config import app, db
from models import MenuItem

@app.route('/admin')
def admin():

    return render_template('admin.html')

@app.route('/add-food-item', methods=['POST'])
def add_food_item():
    data = request.get_json

    if 'name' not in data or 'price' not in data or 'category' not in data:
        return jsonify({"error": "Missing data for name, price or category"}), 400
    
    new_item = MenuItem(name=data['name'], price=data['price'], category=data['category'])
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"message": "Food item added successfully."}), 201

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(debug=True)
