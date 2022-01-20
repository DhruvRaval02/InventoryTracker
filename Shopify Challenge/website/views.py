from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for, Response
from .models import Item
from . import db
import json, io, csv

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
   if request.method == 'POST':
      name = request.form.get('name')
      count = request.form.get('count')
      price = request.form.get('price')

      # Checking for potential invalid data and flashing appropriate error 
      # messages. Otherwise, add created item to database

      if len(count) < 1:
         flash('Invalid Item Count', category='error')
      elif len(name) < 1:
         flash('Item name must be greater than 0 characters', category='error')
      elif len(price) < 1:
         flash('Item Price must be greater than 0', category='error')
      else:
         new_item = Item(name=name, count=count, price=price)
         db.session.add(new_item)
         db.session.commit()
         flash('Item Added!', category='success')

   # Query to get all items in order to render as table in HTML
   all_items = db.session.query(Item).all()

   return render_template("home.html", all_items=all_items)

@views.route('/delete-item', methods=['POST'])
def delete_item():

   # Load deleted item from request and query the id to get full item
   item = json.loads(request.data)
   item_id = item['itemId']
   item = Item.query.get(item_id)

   # If the item exists, delete it from the database
   if item:
      db.session.delete(item)
      db.session.commit()

   return jsonify({})

@views.route('/edit-item', methods=['GET', 'POST'])
def edit_item():

   # Get item id from argument in URL and use it to find full item
   item_id = request.args.get('id')
   item = Item.query.get(item_id)

   if request.method == 'POST':
      name = request.form.get('name')
      count = request.form.get('count')
      price = request.form.get('price')

      # Checking for potential invalid data and flashing appropriate error 
      # messages. Otherwise, add created item to database and delete old item
      # to simulate editing

      if len(count) < 1:
         flash('Invalid Item Count', category='error')
      elif len(name) < 1:
         flash('Item name must be greater than 0 characters', category='error')
      elif len(price) < 1:
         flash('Item Price must be greater than 0', category='error')
      else:
         new_item = Item(name=name, count=count, price=price)
         db.session.delete(item)
         db.session.add(new_item)
         db.session.commit()
         return redirect(url_for('views.home'))
   
   return render_template("edit.html", item=item)

@views.route('/download_csv')
def download_csv():
   data = db.session.query(Item).all()
   output = io.StringIO()
   writer = csv.writer(output)

   # Writing headers for CSV file
   line = ['Item ID', 'Item Name', 'Item Count', 'Unit Price', 'Total Price', 'Date Added']
   writer.writerow(line)

   # Going through each row in table and writing to CSV file
   for row in data:
      total_price = row.price * row.count
      line = [str(row.id), row.name, str(row.count), str(row.price), str(total_price), str(row.date)]
      writer.writerow(line)

   output.seek(0)
   return Response(output, mimetype="text/csv", headers={"Content-disposition":"attachment;filename=inventory.csv"})
