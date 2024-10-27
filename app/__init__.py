# app/__init__.py
from flask import Flask, render_template
from .dfd import create_dfd_app

# Initialize Flask app
flask_app = Flask(__name__)

# Create and initialize Dash app with Flask app reference
dash_app = create_dfd_app(flask_app)

@flask_app.route('/')
def home():
    return render_template('index.html')

@flask_app.route('/dash/')
def dash():
    print("Dash app accessed!")
    return dash_app.index()  # Serve the Dash app


if __name__ == '__main__':
    flask_app.run(debug=True)
