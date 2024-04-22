# import requests

# url = "https://sms-api29.p.rapidapi.com/numbers"

# headers = {
# 	"X-RapidAPI-Key": "2bc9f78becmsh8e0d5d5a833d8bdp1548d2jsne796b338db85",
# 	"X-RapidAPI-Host": "sms-api29.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers)

# print(response.json())

import requests

url = "https://sms-api29.p.rapidapi.com/messages/14046036606"

headers = {
	"X-RapidAPI-Key": "2bc9f78becmsh8e0d5d5a833d8bdp1548d2jsne796b338db85",
	"X-RapidAPI-Host": "sms-api29.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())