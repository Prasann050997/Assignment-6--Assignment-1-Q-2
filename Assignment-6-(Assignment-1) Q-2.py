#Create a dictionary of any 7 Indian states and their capitals. Write this into a JSON file
import json

indian_states = {
    "Gujarat": "Gandhinagar",
    "Madhya Pradesh": "Bhopal",
    "Maharastra": "Mumbai",
    "Uttar Pradesh": "Lucknow",
    "Haryana": "Chandigarh",
    "Rajasthan": "Jaipur",
    "Goa": "Panji",
}

# Create a new json file in write mode to add above data into it.
with open(r"indian_states.json", "w") as file:

    # Write the dictionary to the file in JSON format
    json.dump(indian_states, file)


with open(r"indian_states.json", "r") as file:
    data = file.readlines()
    print(data)
