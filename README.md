# Third Project

##### My Data-Centric Development Project is Hungarian Cuisine.
##### Created with Python, Flask and MnogoDB and the purpose of this project is to create an interactive website with database of recipes that allows the user to create, read, update and delete (CRUD) recipes.

##### This project only for demonstrate the usage of Python language helped by Flask and Jinja and build an interactive application  for certain functionality.
##### Website deployed on Heroku at [Hungarian Cuisine](https://hungarian-cuisine.herokuapp.com/)

## UX

##### Front-end web design built conventional manner and presented by a clear layout. Header section with navigation bar, main section and an informative footer.
##### The project did not required log in functionality and have no restriction at DELETE buttons so please use them wisely.
### User Stories
##### As a user, I want to be able to: 
- **C**reate my own recipes with images.
- **R**ead my own and others recipes.
- **U**pdate or change infromations at recipes.
- **D**elete old or not wanted recipe.
- Find all recipes or organised views for example see recipes by categories.
- Use all functionality at any device

##### As the admin or owner of this page, I want to:
- Able to see all data stored at database by users.
- Modify and use these data from a safe storage.
- Create new functionalities for the page.

## Features
#### Existing Features
##### This webpage is responsive clear view and all buttons and functions working on mobile devices. User of page can create new recipes edit them, create new categories and delet them.
#### Features Left to Implement
##### The delete functionality was more useful if users can delete their only creations so user login would be the solution. At this time only a JavaScript warning ask to be careful with delete.
##### Also another feature idea to put sidebar at base.html for more links and advertisements for business purpose.
## Technologies Used
##### For CSS grid I used Materialize framework and its JQuery.
##### For data transfer Falsk, Jinja, pyMongo and for storage Atlas MongoDB
##### Back-end language is Python. The recipe filter by categories and recipes pagination are the two functionality for demonstrate the understanding the python language and its logic.
# Testing
#### Planning
##### In development I wanted to see all functionalities, design, and responsiveness: after I made some changes at AWS C9 EC2, also put the hosted page under crome developer tool.
##### HTML, CSS code changes was made in Google Crome developer tool and copy and paste back to AWS C9 and after code was pushed also checked at Heroku hosted page.
##### AWS C9 inbuilt hosting feature make ti easy to test every changes promt. During the development I have used this to check back-en and fron-end changes as well.
##### The python terminal and browser console to cach bugs were monitored during development.
##### Family members and friends tested the functionality and responsiveness at different devices sach as Samsung A7 phone, iPhone 8, Samsung tablet, APPLE 13.3, MacBook Air (2017) and Lenovo ideapad 110-15ACL with Widows 10.
#### Manually tested to create a new recipe.
1. Go to New Recipe at navigation bar
2. Fill up the form. HTML validation for filling up all lines can not submit with empty lines
3. For image url With Javascrip there is a defuolt url 
4. Hit submit buttons
5. Go to recipes page at navbar to check your new recipe

##### For edit recipes same form will appear but prefilled lines and can be overwrite those and submit.
# Deployment
##### For deployment I have used Heroku. When I enabled the automated deployment from Heroku after every time the project was pushed to Github, the Heroku automaticly built the new version of the project.
##### [Hungarian Cuisine](https://hungarian-cuisine.herokuapp.com/)
#### How to make difference between the deployed and production version:
##### Secure keys, usernames and passwords in production should be never committed to github. As it suggested the Atlas MongoDB connection string to the .bashrc file:
```
export MONGO_URI = " long string with name and password "
```
##### and put this in the app:
```
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
```
##### To deploy to Heroku I have used AWS Cloud9 IDE to develop this application before deplyment I have turned off Flask debugging by setting debug=False
##### The Requirements file was created with the command:
```
sudo pip3 freeze --local > requirements.txt.
```
##### Followd the videos to create a Procfile: web: python app.py. Through this Heroku find the application.
##### Frequently pushed the codes to GitHub master branch to make sure all changes are safely stored.
##### Database was used MnogoDB as structured: 
```
_id:5d9d159b1e4fa8dcb734f2ca
category_name:"soups and starters"
allergens_types:"milk"
recipe_title:"Cold Fruit Soup"
img_url:"http://rendeles.introcafe.hu/images/products/originals/8.jpg"
recipe_ingredients:"milk, flour, sugar"
recipe_preparation:"boil fruits with sugar add powder and stir"
is_favourite:"on"
```
### Code validation
##### For HTML and CSS language I have used [W3 validator](https://jigsaw.w3.org/css-validator/)
##### for JavaScript language [JSHint](https://jshint.com/) 
### Acknowledgements
## Credits
##### Acknowledgements: Thank you for the help Ali Ashik Mentor reliable and supporting, my slack friends Miklos Sarosi and Dave laffan 
##### Tutor support screen sharing session is very useful at CodeInstitute
##### Content for the text for section recipes was copied from: . Media: images from same website.


