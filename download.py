import requests
import json

r = requests.get('https://www.ebi.ac.uk/emdb/api/search/membrane%20protein%20AND%20database%3A%22EMDB%22%20AND%20structure_determination_method%3A%22singleparticle%22%20AND%20resolution%3A%5B2%20TO%203%7D')

response = r.json()

with open('all.json', 'a') as f:
    f.write(json.dumps(response, indent=2))
