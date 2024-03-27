from flask import Flask, render_template, request, jsonify
from config import app, db
from models import MenuItem


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/', methods=['POST'])
def add_food_item():
    # Retrieve form data
    name = request.json.get('name')
    price = request.json.get('price')
    category = request.json.get('category')

    # Check if all required data is present
    if not name or not price or not category:
        return jsonify({"error": "Missing data for name, price, or category"}), 400

    try:
        # Create new MenuItem object and add it to the session
        new_item = MenuItem(name=name, price=price, category=category)
        db.session.add(new_item)
        db.session.commit()
        return jsonify({"message": "Food item added successfully."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500



@app.route('/menu-item/<int:item_id>')
def get_menu_item(item_id):
    item = MenuItem.query.get(item_id)
    if item:
        return jsonify(item.to_json()), 200
    else:
        return jsonify({"error": "Item not found."}), 404


if __name__ == "__main__":
    with app.app_context():
        db.create_all()


    app.run(debug=True)