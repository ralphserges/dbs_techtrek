from flask import Flask, render_template, request
import requests
import json
import os


app= Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('form.html')

@app.route('/form')
def form_page():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(debug=True)