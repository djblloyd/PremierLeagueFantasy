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
    writer.writerow(('Name','Goals','Form','PointsPerGame', 'Value'))
    for x in range(0, 576):
        writer.writerow((
        data["elements"][x]["web_name"],
        data["elements"][x]["goals_scored"],
        data["elements"][x]["form"],
        data["elements"][x]["points_per_game"],
        data["elements"][x]["now_cost"]))
    
