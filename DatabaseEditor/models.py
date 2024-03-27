from config import db
import time
from sqlalchemy import ForeignKey

class Accounts(db.Model):
    accountID = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(16), nullable=False)

    def to_json(self):
        return{
        "accountID": self.accountID,
        "email": self.email,
        "password": self.password
        }


class Employees(db.Model):
    employeeID = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(100), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    dob = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return{
            "employeeID": self.employeeID,
            "lastName": self.lastName,
            "firstName": self.firstName,
            "dob": self.dob,
            "email": self.email,
            "phoneNumber": self.phoneNumber
        }

class Customers(db.Model):
    customerID = db.Column(db.Integer, primary_key=True)
    lastName = db.Column(db.String(100), nullable=False)
    firstName = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phoneNumber = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return {
            "customerID": self.customerID,
            "lastName": self.lastName,
            "firstName": self.firstName,
            "email": self.email,
            "phoneNumber": self.phoneNumber
        }
    

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "category": self.category
        }


class OrderItem(db.Model):
    purchaseID = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    subTotal = db.Column(db.Float, nullable=False)
    discount = db.Column(db.Float, nullable=False)
    tax = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def to_json(self):
        return {
            "purchaseID": self.purchaseID,
            "date": self.date,
            "subTotal": self.subTotal,
            "discount": self.discount,
            "tax": self.tax,
            "total": self.total
        }
    
class OrderDetails(db.Model):
    purchaseID = db.Column(db.Integer, ForeignKey(OrderItem.purchaseID), primary_key=True)
    id = db.Column(db.Integer, ForeignKey(MenuItem.id), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, ForeignKey(MenuItem.price))
    extendedPrice = db.Column(db.Float, nullable=False)

    def to_json(self):
        return{
            "purchaseID": self.purchaseID,
            "sku": self.id,
            "quantity": self.quantity,
            "price": self.price,
            "extendedPrice": self.extendedPrice
        }

class AddOns(db.Model):
    id = db.Column(db.Float, ForeignKey(MenuItem.id), primary_key=True)
    name = db.Column(db.String(100), ForeignKey(MenuItem.name))

    def to_json(self):
        return{
            "id": self.id,
            "name": self.name
        }

