from flask import Flask, render_template, request, make_response
from requests import Request, Session
import json
import os

app= Flask(__name__)

server_url = "http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/"

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/validation', methods=['GET'])
def login():
    data = {
        'username': 'caritativofiona',
        'password': '922cb712bea79bc8'
    }
    #user_credentials = request.form['input_name'].json()

    request = Request(
        method = 'POST',
        url = server_url + 'login',
        data = data
    )

    prepped = request.prepare()
    session = Session()
    response = session.send(
        prepped
    )

    if response.status_code == 200:
        return response.text
    else:
        return "Bad Request"

    #if user_credentials['user'] != data['user'] or user_credentials['password'] != data['password']:
    #    return make_response('Invalid Credentials', 401, {'WWW-Authenticate' : 'Basic-realm=Login Required!'})
    # Token generation from POSTMAN
    # r = requests.get("http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/login")
    #return "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNhcml0YXRpdm9maW9uYSIsImlhdCI6MTYwMTAwMjIzMywiZXhwIjoxNjAxMDAyODMzLCJpc3MiOiJ0ZWNodHJlazIwMjAifQ.hboi7QHJzzXGUvpb653msp106zOOnL01_Tn_LUrMn78BA1KeAoGuBhgp4Pa11cgJnrsWCok6x0pMxal4AVR9oQ"

@app.route('/logout')
def logout():
    return ''

if __name__ == "__main__":
    app.run(debug=True)
