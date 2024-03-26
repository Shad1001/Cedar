from config import db
import time

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
    purchaseID = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    extendedPrice = db.Column(db.Float, nullable=False)

    def to_json(self):
        return{
            "purchaseID": self.purchaseID,
            "sku": self.sku,
            "quantity": self.quantity,
            "price": self.price,
            "extendedPrice": self.extendedPrice
        }

class Food(db.Model):
    SKU = db.Column(db.Integer, primary_key=True)
    skuDescription = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(100), nullable=False)

    def to_json(self):
        return{
            "SKU": self.SKU,
            "skuDescription": self.skuDescription,
            "price": self.price,
            "category": self.category
        }
    

class AddOns(db.Model):
    SKU = db.Column(db.Integer, primary_key=True)
    skuDescription = db.Column(db.String(100), primary_key=True)

    def to_json(self):
        return{
            "SKU": self.SKU,
            "skuDescription": self.skuDescription
        }

