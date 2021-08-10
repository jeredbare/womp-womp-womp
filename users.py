import requests 
import json
import argparse
import csv

# arguments
endpoints = ["posts", "categories", "tags", "pages", "comments", "taxonomies", "media", "types", "statuses", "settings", "themes", "search", "block-types", "blocks", "block-renderer", "block-directory/search", "plugins", "users"]

parser = argparse.ArgumentParser(description='Enter a URL')
parser.add_argument('Url', metavar='url', type=str, help='The WordPress URL')

args = parser.parse_args()
url_input = args.Url

# endpoints
endpoint_check = requests.get("http://{}/wp-json/wp/v2/".format(url_input))

# checking the status code and the endpoints in wp-json
if endpoint_check.status_code == 200:
    users =[]
    print("\nDiscovered REST API is accessiable at {}".format(url_input) +  " Checking remaining endpoints")
    for i in endpoints:
        checking_status = requests.get("http://{}/wp-json/wp/v2/{}".format(url_input, i))
        print("Endpoint: " + "{}".format(i) + "\n" + "\tHTTP Status Code: " + str(checking_status.status_code))
        if i == "users":
            print("\n" + "*" * 10 + "Users endpoint DETECTED. Users will be enumerated after this check and written to a CSV file."+ "*" * 10 + "\n")

            # function here
            users_endpoint = requests.get("http://{}/wp-json/wp/v2/users/".format(url_input))
            user_json = users_endpoint.json()
            for j in user_json:
                print("ID: " + str(j['id']) + "\n" + "Name: " + j['name'] + "\n" + "Slug: " + j['slug'] + "\n")
                users.append(str(j['slug']))

            # output to csv
            fields = ['Usernames']
            filename = "wordpress_users.csv"
            with open(filename, 'w') as csvfile:
                csvwriter = csv.writer(csvfile)

                csvwriter.writerow(fields)

                # writes the rows
                csvwriter.writerow(users)
            print("Users written to a CSV file.")
else:
    print("Could not connect to the endpoint.")
