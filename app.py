from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import requests
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


@app.route('/')
@app.route('/home')
def home_page():

    url = "http://techtrek2020.ap-southeast-1.elasticbeanstalk.com/validateForm"

    payload = {"customerName":"james",
             "customerAge":"29", 
             "serviceOfficerName":"officer123", 
             "NRIC": "S5454545B", 
             "registrationTime":"25/12/2020 08:12:55", 
             "branchCode":"120", 
             "image":"",
             "productType":["137","070"]}

    token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImNhcml0YXRpdm9maW9uYSIsImlhdCI6MTYwMTAxMDI1MywiZXhwIjoxNjAxMDEwODUzLCJpc3MiOiJ0ZWNodHJlazIwMjAifQ.Ozt4Fi0-9FeE_swLW1Mx-K8WA3f_WyhJxHHnv1nK4mzdLyDn3M5cI7QyjfRQ68rgZq4H0d8lK_YUWsO4JNkVtQ"
    headers = {"Authorization": "Bearer " + token}
    r = requests.post(url, data=payload, headers=headers)

    return str(r.text)


@app.route('/form', methods=['POST','GET'])
def form_page():
    
    return render_template('form.html')

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



    

if __name__ == "__main__":
    app.run(debug=True)