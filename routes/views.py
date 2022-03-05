from flask import jsonify, request, current_app as app
from flask import Flask, render_template, redirect, session, g

@app.route('/')
def home():
    return render_template('index.html')