from django.shortcuts import render
import requests

def home(request):
    url = "https://golf-leaderboard-data.p.rapidapi.com/leaderboard/495"

    headers = {
	    "X-RapidAPI-Key": "889c085e33msh77db1cbd161e461p13fe80jsnd347c15b3383",
	    "X-RapidAPI-Host": "golf-leaderboard-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = response.json()
    return render(request, 'golfprogram/home.html', {
        'first_name': data['first_name']
    })
