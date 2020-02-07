import requests

riot_api_key = 'RGAPI-62da6753-373c-4e3f-b7ea-9117d8b21b39'

def requestChampInfo():
    url = 'https://na1.api.riotgames.com/lol/platform/v3/champion-rotations' + '?' + riot_api_key
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": "RGAPI-62da6753-373c-4e3f-b7ea-9117d8b21b39",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        raise Exception('Bad response code {}'.format(str(response.status_code)))
    return response.json()

def requestSummonerByName(summonerName):
    summonerNameNoSpaces = summonerName.replace(' ', '%20')
    url = 'https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/' + summonerNameNoSpaces + '?' + riot_api_key
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": "RGAPI-62da6753-373c-4e3f-b7ea-9117d8b21b39",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        raise Exception('Bad response code {}'.format(str(response.status_code)))
    return response.json()

def requestLeagueEntriesByEncryptedSummonerId(encryptedSummonerId):
    url = 'https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/' + encryptedSummonerId + '?api_key=' + riot_api_key
    headers = {
        "Origin": "https://developer.riotgames.com",
        "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Riot-Token": "RGAPI-62da6753-373c-4e3f-b7ea-9117d8b21b39",
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:72.0) Gecko/20100101 Firefox/72.0"
    }
    response = requests.get(url=url, headers=headers)
    if response.status_code != 200:
        raise Exception('Bad response code {}'.format(str(response.status_code)))
    return response.json()


print('free champ rotation: ')
print(requestChampInfo())
print('summoner account info: ')
print(requestSummonerByName('C9 Jhin Erso'))
print('summoner league stats: ')
print(requestLeagueEntriesByEncryptedSummonerId(requestSummonerByName('C9 Jhin Erso')['id']))
