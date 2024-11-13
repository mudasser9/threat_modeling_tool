from flask import Flask, render_template, request, redirect, url_for, flash
from app import flask_app
import mysql.connector
from db import get_db_connection

# Route for the login page
@flask_app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate the user
        if authenticate_user(username, password):
            return redirect(url_for('home'))  
        else:
            flash("Invalid username or password", 'danger')
    
    return render_template('home.html')  

# Authentication function
def authenticate_user(username, password):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Query to check if the username and password match
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password))
    user = cursor.fetchone()

    conn.close()

    # Return True if user is found, otherwise False
    return user is not None

# Route for home page after successful login
@flask_app.route('/home')
def home():
    return render_template('home.html')  # Your main page after login
