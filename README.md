# womp-womp-womp
This repository is a python script that will test a WordPress site to see if the WP-JSON endpoint is available.  If the endpoint is available, it will enumerate the users and save them to a CSV file.

# Why
In testing a few WordPress sites, I've constantly noticed the WP-JSON endpoint being open and exposing the users endpoint.  With that endpoint open, you can enumerate all the users and possibly pivot to a spraying or brute force attack.  This is not inherently a threat if you've secured your WordPress site with plugins such as WordFence and/or have a properly configured WAF in front of the site.

# How to use
Install the requests module.
`pip install requirements.txt`

`python users.py [wordpress_domain]`

Example: `python users.py wordpressite.com`

Example Output:
```
Discovered REST API is accessiable at wordpressite.com Checking remaining endpoints
Endpoint: posts
        HTTP Status Code: 200
Endpoint: categories
        HTTP Status Code: 200
Endpoint: tags
        HTTP Status Code: 200
Endpoint: pages
        HTTP Status Code: 200
Endpoint: comments
        HTTP Status Code: 200
Endpoint: taxonomies
        HTTP Status Code: 200
Endpoint: media
        HTTP Status Code: 200
Endpoint: types
        HTTP Status Code: 200
Endpoint: statuses
        HTTP Status Code: 200
Endpoint: settings
        HTTP Status Code: 401
Endpoint: themes
        HTTP Status Code: 401
Endpoint: search
        HTTP Status Code: 200
Endpoint: block-types
        HTTP Status Code: 401
Endpoint: blocks
        HTTP Status Code: 200
Endpoint: block-renderer
        HTTP Status Code: 404
Endpoint: block-directory/search
        HTTP Status Code: 400
Endpoint: plugins
        HTTP Status Code: 401
Endpoint: users
        HTTP Status Code: 200

**********Users endpoint DETECTED. Users will be enumerated after this check and written to a CSV file.**********

ID: 2
Name: User1
Slug: user1

ID: 3
Name: User2
Slug: user2

Users written to a CSV file.

