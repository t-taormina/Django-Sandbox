import requests
import json

url = "https://golf-leaderboard-data.p.rapidapi.com/leaderboard/25"

headers = {
	"X-RapidAPI-Key": "889c085e33msh77db1cbd161e461p13fe80jsnd347c15b3383",
	"X-RapidAPI-Host": "golf-leaderboard-data.p.rapidapi.com"
}

# response = requests.request("GET", url, headers=headers)

file = open('leaderboard.json')

info = json.load(file)

data = info['results']['leaderboard']
print(data[0])
# for i in range(len(data)):
	# print(data[i]['first_name'])


