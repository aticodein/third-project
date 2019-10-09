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
     return render_template("huncuisine.html", myHunCuisineDB=mongo.db.myHunCuisineDB.find(), page_title="Recipes")
                          
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
    
@app.route('/edit_recipe/<myHunCuisineDB_id>')
def edit_recipe(myHunCuisineDB_id):
    the_recipe = mongo.db.myHunCuisineDB.find_one({"_id":ObjectId(myHunCuisineDB_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editrecipe.html", recipe=the_recipe, categories=all_categories, page_title="Edit Recipes")
   
    
if __name__ == '__main__':
    
   app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
          
            