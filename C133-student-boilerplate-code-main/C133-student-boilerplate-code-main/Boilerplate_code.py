#Importing flask module in the project
from flask import Flask

#Create an object of the Flask class
app = Flask(__name__)

#The route() function of the Flask class 
@app.route("/student activity")
def home():
    name="pavan sai"
    age="15"
    return rendertemplate('/student activity.html',student_name=name)
    app.run(debug=True)


#‘/’ URL is bound with first_flask function.
def first_flask():

    return "This is my first flask program"

#run the application on local server
app.run()
