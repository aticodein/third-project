import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'myHunCuisine'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route('/myHunCuisineDB')
def get_myHunCuisineDB():
     return render_template("huncuisine.html", myHunCuisineDB=mongo.db.myHunCuisineDB.find(), page_title="rec ing prep")
                          
@app.route('/categories')
def get_categories():
    return render_template("categories.html", get_categories=mongo.db.categories.find(), page_title="Categories")
   
@app.route('/base')
def get_base():
    return render_template("base.html")
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", get_categories=mongo.db.categories.find(), page_title="Add Recipes")
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    myHunCuisineDB = mongo.db.myHunCuisineDB
    myHunCuisineDB.insert_one(request.form.to_dict())
    return redirect(url_for('get_myHunCuisineDB'))
    
    
if __name__ == '__main__':
    
   app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
          
          
            