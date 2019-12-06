# Third Project

##### My Data-Centric Development Project is Hungarian Cuisine.
##### Created with Python, Flask and MnogoDB and the purpose of this project is to create an interactive website with database of recipes that allows the user to create, read, update and delete (CRUD) recipes.

##### This project only for demonstrate the usage of Python language helped by Flask and Jinja and build an interactive application  for certain functionality.
##### Website deployed at [Hungarian Cuisine](https://hungarian-cuisine.herokuapp.com/)

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

## Features
#### Existing Features
##### This webpage is responsive clear view and all buttons and functions working on mobile devices. User of pge can create new rwcipes edt them, create new categories and delet them.
#### Features Left to Implement
##### The delete functionality was more useful if users can delete their only creations so user login would be the solution.
##### Also another feature idea to put sidebar at base.html for more links and advertisements for business purpose.
#### Technologies Used
##### For CSS grid I used Materialize framework and its own JQuery.
##### For data transfer Falsk, Jinja, pyMongo and for storage Atlas MongoDB
##### Back-end language is Python. The recipe filter by categories and recipes pagination are the two functionality for demonstrate the understanding the python language and its logic.

##### As the admin or owner of this page, I want to:
- Able to see all data stored at database by users.
- Modify and use these data from a safe storage.
- Create new functionalities for the page.

## Deployment
##### For deployment I have used Heroku and installed heroku to Github. This made the checking very easy after every repo push the Heroku automaticly\refereshed the page.
##### [Hungarian Cuisine](https://hungarian-cuisine.herokuapp.com/)
##### How to make difference between the deployed and production version

##### Secure keys, usernames and passwords in production should be never committed to github. As it suggested the Atlas MongoDB connection string to the .bashrc file:

```
export MONGO_URI = " long string with name and password "
```
##### and put this in the app:
```
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
```

## Credits
### Code validation
##### For HTML and CSS language I have used [W3 validator](https://jigsaw.w3.org/css-validator/)
##### for JavaScript language [JSHint](https://jshint.com/) 
### Acknowledgements

##### Thank you for the help Ali Ashik Mentor reliable and supporting, my slack friends Miklos Sarosi and Dave laffan 
##### Tutor support screen sharing session is very useful
##### Thank you
