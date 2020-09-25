from flask import Flask, render_template, request, make_response
import requests
import json
import os
import jwt

app= Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/validation', methods=['GET'])
def login():
    data = {
        "user" : "caritativofiona",
    "password" : "922cb712bea79bc8"
    }

    user_credentials = {
        "user" : 'caritativofiona',
        'password' : '922cb712bea79bc8'
    }

    #user_credentials = request.form['input_name'].json()

    if user_credentials['user'] != data['user'] or user_credentials['password'] != data['password']:
        return make_response('Invalid Credentials', 401, {'WWW-Authenticate' : 'Basic-realm=Login Required!'})
    # Token generation from POSTMAN
    r = requests.get("http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login")
    

    #return "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNhcml0YXRpdm9maW9uYSIsImlhdCI6MTYwMTAwMjIzMywiZXhwIjoxNjAxMDAyODMzLCJpc3MiOiJ0ZWNodHJlazIwMjAifQ.hboi7QHJzzXGUvpb653msp106zOOnL01_Tn_LUrMn78BA1KeAoGuBhgp4Pa11cgJnrsWCok6x0pMxal4AVR9oQ"

@app.route('/logout')
def logout():
    return ''

if __name__ == "__main__":
    app.run(debug=True)