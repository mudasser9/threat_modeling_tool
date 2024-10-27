from flask import Blueprint, render_template, request
from .dfd import create_dfd
from .threats import analyze_threats
from .report import generate_report

main_routes = Blueprint('main', __name__)

@main_routes.route('/')
def index():
    return render_template('index.html')

@main_routes.route('/create_dfd', methods=['POST'])
def create_dfd_route():
    pass

@main_routes.route('/analyze_threats', methods-['POST'])
def analyze_threats_route():
    pass

@main_routes.route('/generate_report', methods=['GET'])
def generate_report_route():
    pass