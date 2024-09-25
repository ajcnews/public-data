import requests
import datetime
import csv

url = "https://services1.arcgis.com/2iUE8l8JKrP2tygQ/ArcGIS/rest/services/Georgia_Power_Outages_View/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&f=json"
response = requests.get(url)
data = response.json()

features = data["features"]

csv_file = f'data/outages_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
csv_columns = ["OBJECTID_1", "NAME", "STATE_NAME", "OutageCount", "CountyStatus", "CustomerCount", "PercentOut", "CountyId", "TimeStamp", "GlobalID", "EditDate"]

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    for feature in features:
        writer.writerow(feature["attributes"])
