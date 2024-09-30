# public-data

This repository contains compilations of public data from different sources used in the AJC's reporting.

## Power Outage Data
_Charles Minshew and Rahul Deshpande, September 2024_

This data collector was developed for our coverage of Hurricane Helene, which struck Florida's 'Big Bend' region as a Category 4 hurricane in September 2024 and then moved northward through Georgia, North Carolina, South Carolina, and Tennessee. Here's a [link to the story](https://www.ajc.com/news/georgia-news/georgia-statewide-power-outage-map-see-outages-by-county-hurricane-helene-updates/KYWHZWRE3RAWLPDF6QOLWLVHUQ/).

We utilized GitHub Actions to automate the updates of both the data and the map every 10 minutes. You can view the workflow file here: [`.github/workflows/update_power_outage_map.yml`](https://github.com/ajcnews/public-data/blob/main/.github/workflows/update_power_outage_map.yml). The map itself was created using Datawrapper, which dynamically updates the visualization based on the raw data provided in this [CSV file](https://raw.githubusercontent.com/ajcnews/public-data/refs/heads/main/power-outages/data/outages.csv).

The `power-outages` directory contains data on power outages in the state of Georgia. The data is from the Georgia Emergency Management and Homeland Security Agency (GEMA) and is updated every 10 minutes. The data is pulled in JSON format before being converted to CSV format using the `convert.py` script. The data contains information for each affected county, including outage count, GEMA's color for county status, customer count, percentage of customers affected, county ID, timestamp, global ID, and edit date.

Example of county data JSON:
```json
{
  "attributes": {
    "OBJECTID_1": 52,
    "NAME": "Fulton",
    "STATE_NAME": "Georgia",
    "OutageCount": 21,
    "CountyStatus": "#004FA2",
    "CustomerCount": 520395,
    "PercentOut": 0.00403539618943303,
    "CountyId": 190,
    "TimeStamp": 1727280278581,
    "GlobalID": "9c03a53a-ae74-499c-b638-9f6781013069",
    "EditDate": 1727280280114
  }
},
```

Example of CSV data:
```csv
objectid_1,name,state_name,outage_count,county_status,customer_count,percent_out,county_id,timestamp,global_id,edit_date
1,Decatur,Georgia,1401,#A19E01,14107,9.931239810023392,174,2024-09-27 01:15:09,4f1c9697-e63e-4cd8-b22f-9aa29ae35cd9,2024-09-27 01:15:10
```
