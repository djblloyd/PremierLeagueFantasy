# Premier-league-fantasy
# Use real premier league data to pick the best fantasy team

# import packages we are going to need
import requests
import json
import csv

# request data using API
resp = requests.get('https://fantasy.premierleague.com/drf/bootstrap-static')

data = resp.json()

# write some key data points to csv file for analysis
with open('eplout.csv','w') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(('Name','Goals','Form','PointsPerGame','Minutes', 'Price'))
    for i in range(len(data["elements"])):        
        writer.writerow((
        data["elements"][i]["web_name"],
        data["elements"][i]["goals_scored"],
        data["elements"][i]["form"],
        data["elements"][i]["points_per_game"],
        data["elements"][i]["minutes"],
        data["elements"][i]["now_cost"]))
    
