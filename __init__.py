"""
The flask application package.
"""

from flask import Flask
from ChartinkAPI import chartink_api

app = Flask(__name__)

app.register_blueprint(chartink_api, url_prefix='/chartink') 
