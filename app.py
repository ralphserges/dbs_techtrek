from flask import Flask, render_template, request, make_response
import requests
import json
import os

app= Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

# @app.route('/test', methods=['POST'])
# def test():
#     r = requests.get("http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login")

#     return r

@app.route('/login', methods=['GET', 'POST'])
def login():
    data = {
        "user" : "caritativofiona",
    "password" : "922cb712bea79bc8"
    }
    user_credentials = request.form['input_name']

    if user_credentials['user'] != data['user'] or user_credentials['password'] != data['password']:
        return make_response('Invalid Credentials', 401, {'WWW-Authenticate' : 'Basic-realm=Login Required!'})

    
    

if __name__ == "__main__":
    app.run(debug=True)