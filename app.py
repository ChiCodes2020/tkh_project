from flask import Flask, render_template, request
import math
import requests
import covid

app = Flask(__name__)



@app.route('/form', methods =['GET', 'POST'])
def get_form():
    if request.method == "GET":
        return f"This is a {request.method} request"

@app.route('/form')
def get_data(covid_data):
    
    return render_template('form.html', covid =covid_data )
 
    

if __name__ == "__main__":
    app.run(debug=True)