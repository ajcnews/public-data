# public-data

This repository contains compilations of public data from different sources used in the AJC's reporting.

## Power Outage Data

The `power-outages` directory contains data on power outages in the state of Georgia. The data is from the Georgia Emergency Management and Homeland Security Agency (GEMA/HS) and is updated every 10 minutes. The data is pulled in JSON format before being converted to CSV format. The data contains information for each affected county; outage count, color county status, customer count, percentage of customers affected, county ID, timestamp, global ID, and edit date.

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
