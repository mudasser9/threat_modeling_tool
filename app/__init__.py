from flask import Flask, render_template
from .dfd import create_dfd_app
import mysql.connector



# Initialize Flask app
flask_app = Flask(__name__)

# Create and initialize Dash app with Flask app reference
dash_app = create_dfd_app(flask_app)



# Function to get a database connection
def get_db_connection():
    try:
        return mysql.connector.connect(**db_config)
    except mysql.connector.Error as err:
        print(f"Database connection error: {err}")
        return None

# Flask route for the home page
@flask_app.route('/')
def home():
    return render_template('app/static/home.html')

# Flask route for the Dash app
@flask_app.route('/dash/')
def dash():
    print("Dash app accessed!")
    return dash_app.index()  # Serve the Dash app

# Example of connecting to the database on start
try:
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        # Add your database queries here
        conn.close()  # Close the connection after usage
except mysql.connector.Error as err:
    print(f"Database initialization error: {err}")

if __name__ == '__main__':
    flask_app.run(debug=True)
