from . import db
from sqlalchemy.sql import func

class Item(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(10000))
   count = db.Column(db.Integer)
   price = db.Column(db.Integer)
   date = db.Column(db.DateTime(timezone=True), default=func.now())