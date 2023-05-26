import csv
import json

def convert_csv_to_json(csv_file, json_file):
    # Read CSV file and initialize data dictionary
    data = []
    with open(csv_file, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    
    # Write data to JSON file
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

# Replace 'input.csv' and 'output.json' with your desired filenames
csv_file = 'input.csv'
json_file = 'output.json'

convert_csv_to_json("FrontdoorTweets.csv","frontdoorTweets.json")

