from flask import jsonify, request, current_app as app
from flask import Flask, render_template, redirect, session, g

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/discover')
def discover():
    return render_template('discover.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/sample-business-page-1')
def page():
    return render_template('sample-business-page-1.html')

@app.route('/sample-business-page')
def products():
    return render_template('sample-business-page.html')