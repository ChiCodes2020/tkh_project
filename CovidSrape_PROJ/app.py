from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import requests
import covid


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f"<Visitor {self.id} {self.name} {self.email} {self.message}>"


# @app.route('/form', methods =['GET', 'POST'])
# def get_form():
#     if request.method == "GET":
#         return f"This is a {request.method} request"

# @app.route('/form')
# def get_data(covid_data):
    
#     return render_template('form.html', covid =covid_data )

@app.route('/admin')
def admin():
    usrs = User.query.all()
    return render_template("admin.html", users=usrs)

@app.route('/', methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':
        user_name = request.form['name']
        user_email = request.form['email'] 
        user_message = request.form['text'] 

        user = User(name=user_name, email= user_email, message = user_message )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('contact_me'))
    return render_template('home.html')
 
    

if __name__ == "__main__":
    db.drop_all()
    db.create_all()
    app.run(debug=True)