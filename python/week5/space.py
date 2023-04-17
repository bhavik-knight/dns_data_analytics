import requests

URI: str = "http://api.open-notify.org/astros.json"

response = requests.get(URI)

# we want name of all people in the space
# convert response into JSON format: .json() method
# response.json() returns a JSON object where we can search for "people"
# "people" is a list of dictionaries, we can look for "name" in this dictionary for one name
# we can use `map(function, iterables)`, and list the object return by map
# where iterables is list of dictionary mentioned above
# where function is a anonymous function lambda, which gets the value of key "name"
names = list(map(lambda x: x.get("name") , response.json().get("people")))
print(names)