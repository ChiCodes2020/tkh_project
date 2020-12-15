from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests


app = Flask(__name__)

app.config["ENV"] = 'development'
app.config["SECRET_KEY"]=b'_5#y2L"F4Q8z\n\xec]/'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///chioma-nitter.db'
# this line is to prevent SQLAlchemy from throwing a warning
# if you don't get one with out it, feel free to remove
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#
# DB SETUP
# 

# this set's up our db connection to our flask application
db = SQLAlchemy(app)

# this is our model (aka table)
class TweetTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweets = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
      
#
# VIEWS 
#


# set up your index view to show your "home" page
# it should include:
# links to any pages you have
# information about your data
# information about how to access your data
# you can choose to output data on this page
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# include other views that return html here:
@app.route('/other')
def other_route():
    table = TweetTable.query.all()
    d = []
    for row in table:
        row_as_dict ={
            "tweet": row.tweets,
            "likes": row.likes,
        }
        d.append(row_as_dict)
    return render_template('other.html', data = d)


@app.route('/api', methods=['GET'])
def api_route():
    table = TweetTable.query.all()
    d = []
    for row in table:
        row_as_dict ={
            "tweet": row.tweets,
            "likes": row.likes,
        }
        d.append(row_as_dict)
    return d


    # table = TweetTable.query.all()
    # d = {row.tweets:row.likes for row in table}
    # return jsonify(d)


# @app.route('/api', methods=['POST'])
# def add_data():
#     for k,v in request.args.items():
#         pass
#     return jsonify({})
        
# # change this to allow the deletion of data
# @app.route('/api', methods=['DELETE'])
# def delete_data():
#     for k,v in request.args.items():
#         pass
#     return jsonify({})


if __name__ == '__main__':
    app.run(debug=True)