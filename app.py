from flask import Flask, render_template, request
import requests
from flask import Flask, render_template, request, make_response
from requests import Request, Session
from flask_sqlalchemy import SQLAlchemy
import json
import os

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) 


class Customer_DB(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    cust_name = db.Column(db.String(64), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    product_type = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.cust_name}','{self.age}', '{self.image_file}', '{self.product_type}')"

server_url = "http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/"

def get_token():
    
    payload = {
        "username" : "caritativofiona",
        "password" : "922cb712bea79bc8"
    }
    url = server_url+"login" 
    r = requests.post(url, data=payload)
    return r.text


@app.route('/')
@app.route('/login')
def login_page():
    return render_template("login.html")
    
   
@app.route('/form', methods=['POST','GET'])
def form_page():
    username = request.form['username']
    return render_template('form.html', username=username)


@app.route('/userconfirm', methods=['POST'])
def user_confirm():
    cust_name = request.form['customer_name']
    customer_age = request.form['customer_age']
    officer_name = request.form['officer_name']
    nric = request.form['customer_nric']
    reg_time = request.form['reg_time']
    branch_code = request.form['branch_code']
    image = request.form['image']
    productType = request.form['productType']
    
    #customer = Customer_DB(cust_name, age, image_file, product_type)
    #db.session.add(customer)
    #db.session.commit()
   
    return render_template('userconfirm.html', user=cust_name)

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
        token = response.text
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
'''
 url = "http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/validateForm"

    payload = {
            "customerName":"james",
             "customerAge":"29", 
             "serviceOfficerName":"officerjohn", 
             "NRIC": "S5454545B", 
             "registrationTime":"25/12/2020 08:12:55", 
             "branchCode":"7171", 
             "image":"",
             "productType":["Investor","Insurance"]
    }

    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNhcml0YXRpdm9maW9uYSIsImlhdCI6MTYwMTAxMjQ3OCwiZXhwIjoxNjAxMDEzMDc4LCJpc3MiOiJ0ZWNodHJlazIwMjAifQ.hHn78450WsIOTn59u6lPPZCsmhMQfCrFeT6Qlf656Pxo8mu8Gry5-O6b-uaiqXUM3BPaDznRuXSG2Qgwoe1uDg"
    headers = {"Authorization": "Bearer " + token}
    r = requests.post(url, data=payload, headers=headers)
    
    return str(get_token())

'''