from config import db
import time

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
