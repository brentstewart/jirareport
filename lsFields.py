import requests

# Jira API base URL
print("Your Jira Cloud URL should look something like yourcompany.atlassian.com")
BASE_URL = input("Jira Cloud URL:")
BASE_URL = BASE_URL + "/rest/api/2"

# Jira credentials
USERNAME= input("Username: ")
print("--------------------------------------------------------")
print("Next you'll be asked for an API token.  If you don't have a token, here's how to set one up.")
print("1. In Jira, click your picture in the upper right and choose _manage account_")
print("2. In the profile page, choose the Security tab on the top.")
print("3. Under Security, go to Create and manage API tokens")
print("--------------------------------------------------------")
API_TOKEN = input("Please enter your Jira API Token: ")

# Create a session with basic authentication
session = requests.Session()
session.auth = (USERNAME, API_TOKEN)

# Make a GET request to retrieve all available fields
response = session.get(f"{BASE_URL}/field")

print("{:<40}{:<30}".format("#Name", "ID"))
if response.status_code == 200:
    fields = response.json()
    for field in fields:
        print("{:<40}{:<30}".format(str(field['name']),str(field['id'])))
else:
    print(f"Failed to fetch fields: {response.status_code}")
