import requests

riot_api_key = 'RGAPI-62da6753-373c-4e3f-b7ea-9117d8b21b39'
riot_champInfo_url = 'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations'
riot_champInfo_request_url = riot_champInfo_url + '?' + riot_api_key
riot_champInfo_request_headers = {
    "Origin": "https://developer.riotgames.com",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Riot-Token": "RGAPI-62da6753-373c-4e3f-b7ea-9117d8b21b39",
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
}
response = requests.get(url=riot_champInfo_request_url, headers=riot_champInfo_request_headers)
if response.status_code != 200:
	raise Exception('Bad response code {}'.format(str(response.status_code)))
json_response = response.json()
print(json_response)
freeChampionIds = json_response['freeChampionIds']
print(freeChampionIds)
freeChampionIdsForNewPlayers = json_response['freeChampionIdsForNewPlayers']
print(freeChampionIdsForNewPlayers)
maxNewPlayerLevel = json_response['maxNewPlayerLevel']
print(maxNewPlayerLevel)
