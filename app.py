import math
import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)


app.config["MONGO_DBNAME"] = 'myHunCuisine'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')

mongo = PyMongo(app)

@app.route('/')
@app.route("/index", methods=['POST'])

def get_index():
    
    get_categories = mongo.db.categories.find()
    
    
    # Pagination

    current_page = int(request.args.get('current_page', 1))
    recipes_per_page=4
    total_recipes = mongo.db.myHunCuisineDB.count()
    num_pages = range(1, int(math.ceil(total_recipes / recipes_per_page)) + 1)
    
    
    recipes = mongo.db.myHunCuisineDB.find().skip(
       (current_page - 1) * recipes_per_page).limit(recipes_per_page)
    
    
  
    # Summary - (example) 'showing 1 - 4 of all results'
    x = current_page * recipes_per_page
    first_result_num = x - recipes_per_page + 1
    last_result_num = x if x < total_recipes else total_recipes
    
    #filter_category = request.args.to_dict()
    
   

    return render_template('index.html',
                           myHunCuisineDB=mongo.db.myHunCuisineDB.find(),
                           categories=mongo.db.categories.find(),
                           recipes=recipes,
                           get_categories=get_categories,
                           # Pagination & Sumarry
                           current_page=current_page,
                           pages=num_pages,
                           first_result_num=first_result_num,
                           last_result_num=last_result_num,
                           page_title="Main Page")

@app.route('/recipes')
def get_recipes():
  
    filter ={}
    
   
    filter = request.args.to_dict()

    
    
    recipes = mongo.db.myHunCuisineDB.find(filter)
    get_categories = mongo.db.categories.find()
    
    
    return render_template("recipes.html",
                            get_categories=get_categories,
                            recipes=recipes,
                            page_title="Recipes") 
    
@app.route('/myHunCuisineDB')
def get_myHunCuisineDB():
    return render_template("huncuisine.html", myHunCuisineDB=mongo.db.myHunCuisineDB.find(), page_title="Edit Recipes")
     
@app.route('/get_categories')
def get_categories():
    return render_template('managecat.html', categories=mongo.db.categories.find())
    
@app.route('/get_categories_only')
def get_categories_only():
    return render_template('categories.html', categories=mongo.db.categories.find())
    
@app.route('/get_allergens_only')
def get_allergens_only():
    return render_template('allergens.html', allergens=mongo.db.allergens.find())    
    
@app.route('/get_allergens')
def get_allergens():
    return render_template('manageallergens.html', allergens=mongo.db.allergens.find())
    
@app.route('/get_images')
def get_images():
    return render_template('index.html', images=mongo.db.img_url.find())    
                          
@app.route('/base')
def get_base():
    return render_template("base.html")
    
print(get_index)    
    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", get_categories=mongo.db.categories.find(), allergens=mongo.db.allergens.find(), page_title="Add Your New Recipe")
    
@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    myHunCuisineDB = mongo.db.myHunCuisineDB
    myHunCuisineDB.insert_one(request.form.to_dict())
    my_data = request.form.to_dict()
    recipe_ingredients = [mongo.db.recipe_ingredients.split]
    
    print(recipe_ingredients)
    return redirect(url_for('get_myHunCuisineDB'))
    
@app.route('/insert_category', methods=['POST'])    
def insert_category():
    categories = mongo.db.categories
    categories.insert_one(request.form.to_dict())
   # category_doc = {'category_name': request.form.get['category_name']}
   # categories.insert_one(category_doc)
    return redirect(url_for('get_categories'))
    
@app.route('/insert_allergens', methods=['POST'])    
def insert_allergens():
    allergens = mongo.db.allergens
    allergens.insert_one(request.form.to_dict())
   
    return redirect(url_for('get_allergens'))     
    
@app.route('/new_gategory')
def new_gategory():
    return render_template('addcategory.html')
    
@app.route('/new_allergens')
def new_allergens():
    return render_template('addallergens.html')    
    
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.myHunCuisineDB.find_one({"_id":ObjectId(recipe_id)})
    return render_template('editrecipe.html', recipe=the_recipe, get_categories=mongo.db.categories.find(), allergens=mongo.db.allergens.find(), page_title="Edit Recipes")

@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.categories.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('get_categories'))
    
@app.route('/update_allergens/<allergens_id>', methods=['POST'])
def update_allergens(allergens_id):
    mongo.db.allergens.update(
        {'_id': ObjectId(allergens_id)},
        {'allergens_types': request.form.get('allergens_types')})
    return redirect(url_for('get_allergens'))    
    
@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipe = mongo.db.myHunCuisineDB
    category = mongo.db.categories
    allergens = mongo.db.allergens
    recipe.update( {'_id': ObjectId(recipe_id)},
    {
        'category_name':request.form.get('category_name'),
        'allergens_types':request.form.get('allergens_types'),
        'recipe_title':request.form.get('recipe_title'),
        'img_url': request.form.get('img_url'),
        'recipe_ingredients': request.form.get('recipe_ingredients'),
        'recipe_preparation': request.form.get('recipe_preparation'),
        'is_favourite':request.form.get('is_favourite')
    })
    return redirect(url_for('get_myHunCuisineDB')) 
    
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.myHunCuisineDB.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('get_myHunCuisineDB'))
    
@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.categories.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('get_categories'))    
    
@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    return render_template('editcategory.html',
                           category=mongo.db.categories.find_one(
                           {'_id': ObjectId(category_id)}))
    
    
@app.route('/delete_allergens/<allergens_id>')
def delete_allergens(allergens_id):
    mongo.db.allergens.remove({'_id': ObjectId(allergens_id)})
    return redirect(url_for('get_allergens'))  
    
    
@app.route('/edit_allergens/<allergens_id>')
def edit_allergens(allergens_id):
    return render_template('editallergens.html',
                           allergens=mongo.db.allergens.find_one(
                           {'_id': ObjectId(allergens_id)}))                           
 
@app.route('/filter_by_category/<selected_category>')
def filter_by_category(selected_category):
    selected_category = mongo.db.categories.find({"_id":ObjectId()})
    return render_template('editrecipe.html', get_categories=mongo.db.categories.find(), page_title="Select By Category")
 
   
    
if __name__ == '__main__':
    
   app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)