from flask import Flask, render_template, request, redirect, session, url_for
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"

#@app.route('/initialize-cart', methods=['POST'])
#def initialize_cart():

#cart = []
    
#@app.route('/add-to-cart', methods=['POST'])
#def add_to_cart():
    
              
#@app.route('/remove-from-cart', methods=['POST'])
#def delete_cart_item():


#@app.route('/order-confirmation', methods=['GET'])
#def order_confirmation():
    # after an order is finished this saves the final state the cart to the database
    # when the user finishs an order this displays as their receipt and will also show up in their user dashboard

if __name__ == '__main__':
    app.run(debug=True)