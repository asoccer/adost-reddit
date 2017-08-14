import sys,requests,pprint

def main(argv):
    user = argv[0]
    url = "https://reddit.com/u/" + str(user) + ".json"
    headers = {'User-Agent': "Get User Profile"}
    data = requests.get(url=url,headers=headers)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(data.json()['data']['children'][0]['data'])
    

if __name__ == "__main__":
   main(sys.argv[1:])

