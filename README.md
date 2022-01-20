# InventoryTracker
A Flask web application used to simulate an inventory tracking system. Created for Shopify's 2022 summer backend developer intern challenge.

# Setup and Installation:

Navigate to the desired space in your computer and clone this repository with `git clone <repository URL>`

Make sure that you have the latest version of python3 and pip3 installed. To do this, navigate to https://www.python.org/downloads/ and install the correct version based on your operating system. To enable pip3, navigate to the directory of this project and run `python3 -m ensurepip`. Then, in that same directory, run the following commands to install Flask and SQL-Alchemy:

   `pip3 install flask`

   `pip3 install flask-sqlalchemy`
   
# Running the Application:

`python3 main.py` or run `main.py` in desired code editor

# Using the Application:

The homepage has the list view of all of our current entries in the table at the top, as well as an option to download the table into a .csv file. On the table, we have options to edit or delete the item entry, as well as the item’s name, count, unit price, and total price. 

If we click on the button used for editing an item, we are taken to another page where that item’s information is pre-filled and we can edit it to our liking. 

Scrolling down on the homepage, we have the option to create a new item for our table by filling out an HTML form. Once we submit this form, our page will automatically update to reflect this item in the table above.
