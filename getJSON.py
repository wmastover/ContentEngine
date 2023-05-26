import json


def getJSON(path): 
    # Specify the path to your JSON file
    json_file_path = path

    # Specify the path to your JSON file

    # Open the JSON file for reading
    with open(json_file_path, "r") as json_file:
        # Load the contents of the file as a JSON object
        json_data = json.load(json_file)

        # Convert the JSON object to a string
        json_string = json.dumps(json_data)

        # Return the JSON data as a string
        return json_string
