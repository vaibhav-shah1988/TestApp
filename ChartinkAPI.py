import flask
from flask import request, Blueprint  
import json  
import requests_html

chartink_api = Blueprint('chartink_api', __name__)  
 
@chartink_api.route("/get", methods=['GET'])  
def getChartInkStocks():

    query_parameters = request.args
    link = query_parameters.get('link')

    session = requests_html.HTMLSession()
    r = session.get(link)
    r.html.render()
    items = r.html.find("table#DataTables_Table_0",first=True)
    list = []
    for item in items.find("tr"):
    	data = [td.text for td in item.find("th,td")]
    	list.append(json.dumps(data))
       
    return json.dumps(list)
