import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'myHunCuisine'
app.config["MONGO_URI"] = 'mongodb+srv://ati_user:Zxcv4542@hungariancuisine-7dmod.mongodb.net/myHunCuisine?retryWrites=true&w=majority'

mongo = PyMongo(app)

@app.route('/')
@app.route('/myHunCuisineDB')
def get_myHunCuisineDB():
    return render_template("huncuisine.html", myHunCuisineDB=mongo.db.myHunCuisineDB.find())
    

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            