import requests
from datetime import datetime
import csv
import shutil
from zoneinfo import ZoneInfo

url = "https://services1.arcgis.com/2iUE8l8JKrP2tygQ/ArcGIS/rest/services/Georgia_Power_Outages_View/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&f=json"
response = requests.get(url)
data = response.json()

features = data["features"]

csv_file = f'data/outages.csv'
csv_columns = ["objectid_1", "name", "state_name", "outage_count", "county_status", "customer_count", "percent_out", "county_id", "timestamp", "global_id", "edit_date"]

utc_zone = ZoneInfo("UTC")
ny_zone = ZoneInfo("America/New_York")

with open(csv_file, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()
    for feature in features:
        attributes = feature["attributes"]

        attributes["objectid_1"] = attributes.pop("OBJECTID_1")
        attributes["name"] = attributes.pop("NAME")
        attributes["state_name"] = attributes.pop("STATE_NAME")
        attributes["outage_count"] = attributes.pop("OutageCount")
        attributes["county_status"] = attributes.pop("CountyStatus")
        attributes["customer_count"] = attributes.pop("CustomerCount")
        attributes["percent_out"] = attributes.pop("PercentOut")
        attributes["county_id"] = attributes.pop("CountyId")
        attributes["global_id"] = attributes.pop("GlobalID")

        attributes["timestamp"] = datetime.fromtimestamp(attributes.pop("TimeStamp") / 1000.0).replace(tzinfo=utc_zone).astimezone(ny_zone).strftime("%Y-%m-%d %H:%M:%S")

        attributes["edit_date"] = datetime.fromtimestamp(attributes.pop("EditDate") / 1000.0).replace(tzinfo=utc_zone).astimezone(ny_zone).strftime("%Y-%m-%d %H:%M:%S")

        writer.writerow({key: attributes[key] for key in csv_columns})

shutil.copy(csv_file, f"data/outages_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv")
